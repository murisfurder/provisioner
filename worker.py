from lib import ansible_helper
from lib import redis_helper
from lib import doc_parser
import os
import settings
import time


def has_ssh_keys():
    """
    This will return true if no key is set.
    """
    return bool(settings.SSH_PRIVATE_KEYS)


def prepare_ssh():
    ssh_dir = '/root/.ssh'
    known_hosts_file = os.path.join(ssh_dir, 'known_hosts')
    id_rsa = os.path.join(ssh_dir, 'id_rsa')
    ssh_keys = settings.SSH_PRIVATE_KEYS

    # SSH is picky with permissions.
    if not os.path.isdir(ssh_dir):
        os.mkdir(ssh_dir)
    os.chmod(ssh_dir, 0700)

    # Clear out any old hosts to avoid
    # potential conflicts.
    if os.path.isfile(known_hosts_file):
        os.remove(known_hosts_file)

    if has_ssh_keys():
        with open(id_rsa, 'wb') as f:
            f.write('{}\n'.format(ssh_keys))
        os.chmod(id_rsa, 0600)


def task_router(task):
    """
    Task router, with sanity check
    """

    error_msg = None

    # Define and lookup the required variables
    attempts = task.get('attempts')
    role = task.get('role')
    uuid = task.get('uuid')
    username = task.get('username', settings.REMOTE_USER)
    password = task.get('password')
    target_ip = task.get('ip')
    extra_vars = task.get('extra_vars')
    only_tags = task.get('only_tags')
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
    if not ((password or has_ssh_keys()) and target_ip and role):
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

    if role in settings.MODULES:
        if role == 'ping':
            run_module = ansible_helper.ping_vm(
                remote_user=username,
                remote_pass=password,
                inventory=inventory
            )
        elif role == 'ssh-keys':
            run_module = ansible_helper.install_ssh_keys(
                remote_user=username,
                remote_pass=password,
                inventory=inventory,
                extra_vars=extra_vars,
            )

        if len(run_module['dark']) > 0:
            failed = True
            error_msg = run_module['dark'][target_ip].get('msg')

        if run_module['contacted'] > 0:
            failed = run_module['contacted'][target_ip].get('failed')
            error_msg = run_module['contacted'][target_ip].get('msg')

        if failed:
            task['last_update'] = str(time.mktime(time.gmtime()))
            redis_helper.update_status(
                uuid=uuid,
                msg=error_msg,
            )
            redis_helper.add_to_queue(task)
            print 'Failed provisioning {} for {}@{} (uuid: {})'.format(
                role,
                username,
                target_ip,
                uuid,
            )
            return

    elif role in settings.PLAYBOOKS:
        run_playbook = ansible_helper.provision(
            remote_user=username,
            remote_pass=password,
            inventory=inventory,
            role=role,
            extra_vars=extra_vars,
            only_tags=only_tags,
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
        redis_helper.update_status(
            uuid=uuid,
            msg='Unknown role/playbook: {}'.format(role)
        )
        return

    redis_helper.update_status(
        uuid=uuid,
        attempts=attempts,
        status='Done',
        install_notes=doc_parser.get_docs(
            role=role,
            extra_vars=extra_vars
        )
    )

    print 'Done provisioning {} for {}@{} (uuid: {})'.format(
        role,
        username,
        target_ip,
        uuid,
    )


def main():
    while True:
        prepare_ssh()
        task = redis_helper.pop_from_queue()

        if task:
            task_router(task)
        time.sleep(1)

if __name__ == '__main__':
    main()
