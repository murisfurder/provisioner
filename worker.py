from lib import ansible_helper
from lib import redis_helper
import time


def key_lookup(data, key):
    """
    Returns the value as string or False.
    """

    if key not in data:
        print 'Key {} is missing.'.format(key)
        return False

    return str(data[key])


def task_router(task):
    """
    Task router, with sanity check
    """

    # Make sure there is at least 30 seconds between retries.
    # If not, pop it back into the queue
    if task['last_update']:
        last_update = float(task['last_update'])
        if last_update + 30 >= time.mktime(time.gmtime()):
            redis_helper.add_to_queue(task)
            return

    task['attempts'] += 1

    # Define and lookup the required variables
    attempts = task['attempts']
    role = key_lookup(task, 'role')
    uuid = key_lookup(task, 'uuid')
    username = key_lookup(task, 'username')
    password = key_lookup(task, 'password')
    target_ip = key_lookup(task, 'ip')

    # Make sure we received all required fields
    if not (username and password and target_ip and role):
        return False

    # Give it maximum three attempts
    if task['attempts'] > 3:
        print 'Too many attempts for {}@{} (uuid: {})'.format(
            username,
            target_ip,
            uuid
        )
        redis_helper.push_status(
            role=role,
            uuid=uuid,
            ip=target_ip,
            attempts=attempts,
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

    redis_helper.push_status(
        role=role,
        uuid=uuid,
        ip=target_ip,
        attempts=attempts,
        status='Provisioning'
    )

    inventory = ansible_helper.generate_inventory(
        target_ip=target_ip
    )

    # @TODO add:
    # * Registry
    # * PostgreSQL

    playbooks = [
        'cloudcompose',
        'docker',
        'mongodb',
        'mysql',
        'redis',
        'wordpress',
    ]

    if role == 'ping':
        run_ping = ansible_helper.ping_vm(
            remote_user=username,
            remote_pass=password,
            inventory=inventory
        )
        if not run_ping:
            print '{} is *not* running'.format(target_ip)
            task['last_update'] = str(time.mktime(time.gmtime()))
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

    redis_helper.push_status(
        role=role,
        uuid=uuid,
        ip=target_ip,
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