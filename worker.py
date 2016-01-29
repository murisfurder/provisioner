from lib import ansible_helper
from lib import redis_helper
import time


def task_router(task):
    """
    Task router, with sanity check
    """

    # Define and lookup the required variables
    attempts = task.get('attempts')
    role = task.get('role')
    uuid = task.get('uuid')
    username = task.get('username')
    password = task.get('password')
    target_ip = task.get('ip')
    extra_vars = task.get('extra_vars')
    status = redis_helper.get_status(uuid)

    if status['status'] == 'Aborted':
        return

    # Make sure there is at least 30 seconds between retries.
    # If not, pop it back into the queue
    if task.get('last_update'):
        last_update = float(task['last_update'])
        if last_update + 30 >= time.mktime(time.gmtime()):
            redis_helper.add_to_queue(task)
            return

    attempts += 1
    task['attempts'] = attempts

    # Make sure we received all required fields
    if not (username and password and target_ip and role):
        return False

    # Give it maximum three attempts
    if attempts > 3:
        print 'Too many attempts for {}@{} (uuid: {})'.format(
            username,
            target_ip,
            uuid
        )
        redis_helper.update_status(
            uuid=uuid,
            status='Failed'
        )
        return False

    print 'Got task \'{}\' for {}@{} (attempt: {}, uuid: {})'.format(
        role,
        username,
        target_ip,
        attempts,
        uuid,
    )

    redis_helper.update_status(
        uuid=uuid,
        attempts=attempts,
        status='Provisioning'
    )

    inventory = ansible_helper.generate_inventory(
        target_ip=target_ip
    )

    playbooks = [
        'cloudcompose',
        'docker',
        'mongodb',
        'mysql',
        'redis',
        'wordpress',
    ]

    if role == 'ping':
        run_module = ansible_helper.ping_vm(
            remote_user=username,
            remote_pass=password,
            inventory=inventory
        )

        if len(run_module['dark']) > 0:
            task['last_update'] = str(time.mktime(time.gmtime()))
            redis_helper.update_status(
                uuid=uuid,
                msg=run_module['dark'][target_ip]['msg']
            )
            redis_helper.add_to_queue(task)
            print 'Failed provisioning {} for {}@{} (uuid: {})'.format(
                role,
                username,
                target_ip,
                uuid,
            )
            return

    elif role == 'ssh-keys':
        run_module = ansible_helper.install_ssh_keys(
            remote_user=username,
            remote_pass=password,
            inventory=inventory,
            extra_vars=extra_vars,
        )

        if len(run_module['dark']) > 0:
            task['last_update'] = str(time.mktime(time.gmtime()))
            redis_helper.update_status(
                uuid=uuid,
                msg=run_module['dark'][target_ip]['msg']
            )
            redis_helper.add_to_queue(task)
            print 'Failed provisioning {} for {}@{} (uuid: {})'.format(
                role,
                username,
                target_ip,
                uuid,
            )
            return

    elif role in playbooks:
        run_playbook = ansible_helper.provision(
            remote_user=username,
            remote_pass=password,
            inventory=inventory,
            role=role
        )
        if not (
            run_playbook[target_ip]['unreachable'] == 0 and
            run_playbook[target_ip]['failures'] == 0
        ):
            task['last_update'] = str(time.mktime(time.gmtime()))
            redis_helper.add_to_queue(task)
            print 'Failed provisioning {} for {}@{} (uuid: {})'.format(
                role,
                username,
                target_ip,
                uuid,
            )
            return
    else:
        print 'Unknown role/playbook: {}'.format(role)
        return

    redis_helper.update_status(
        uuid=uuid,
        attempts=attempts,
        status='Done'
    )

    print 'Done provisioning {} for {}@{} (uuid: {})'.format(
        role,
        username,
        target_ip,
        uuid,
    )


def main():
    while True:
        task = redis_helper.pop_from_queue()

        if task:
            task_router(task)
        time.sleep(1)

if __name__ == '__main__':
    main()
