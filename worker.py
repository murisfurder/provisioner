from lib import ansible_helper
from lib import redis_helper
import time


def task_router(task):
    """
    Task router for Redis tasks, with sanity check
    """

    def data_sanitizer(data, key, expected_type):
        """
        Sanity check the data against expected data type
        Returns the value or False.
        """

        if key not in data:
            return False

        # @TODO fix me.
        # if not type(data[key]) is expected_type:
        #    return False

        return data[key]

    task['attempts'] += 1

    # Define and lookup the required variables
    attempts = task['attempts']
    role = data_sanitizer(task, 'role', type(''))
    uuid = data_sanitizer(task, 'uuid', type(''))
    username = data_sanitizer(task, 'username', type(''))
    password = data_sanitizer(task, 'password', type(''))
    target_ip = data_sanitizer(task, 'ip', type(''))

    # Make sure we received all required fields
    if not (username and password and target_ip and role):
        print 'Missing required value'
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
    # * Wordpress
    # * Registry
    # * Redis
    # * MongoDB
    # * MySQL
    # * PostgreSQL

    if role == 'ping':
        run_ping = ansible_helper.ping_vm(
            remote_user=username,
            remote_pass=password,
            inventory=inventory
        )
        if not run_ping:
            print '{} is *not* running'.format(target_ip)
            redis_helper.add_to_queue(task)
            print 'Failed provisioning {} for {}@{} (uuid: {})'.format(
                role,
                username,
                target_ip,
                uuid,
            )
            return
    elif role == 'docker':
        run_playbook = ansible_helper.provision_docker(
            remote_user=username,
            remote_pass=password,
            inventory=inventory,
        )
        if not (
            run_playbook[target_ip]['unreachable'] == 0 and
            run_playbook[target_ip]['failures'] == 0
        ):
            redis_helper.add_to_queue(task)
            print 'Failed provisioning {} for {}@{} (uuid: {})'.format(
                role,
                username,
                target_ip,
                uuid,
            )
            return
    elif role == 'wordpress':
        run_playbook = ansible_helper.provision_wordpress(
            remote_user=username,
            remote_pass=password,
            inventory=inventory,
        )
        if not (
            run_playbook[target_ip]['unreachable'] == 0 and
            run_playbook[target_ip]['failures'] == 0
        ):
            redis_helper.add_to_queue(task)
            print 'Failed provisioning {} for {}@{} (uuid: {})'.format(
                role,
                username,
                target_ip,
                uuid,
            )
            return
    elif role == 'cloudcompose':
        run_playbook = ansible_helper.provision_cloudcompose(
            remote_user=username,
            remote_pass=password,
            inventory=inventory,
        )
        if not (
            run_playbook[target_ip]['unreachable'] == 0 and
            run_playbook[target_ip]['failures'] == 0
        ):
            redis_helper.add_to_queue(task)
            print 'Failed provisioning {} for {}@{} (uuid: {})'.format(
                role,
                username,
                target_ip,
                uuid,
            )
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
        else:
            time.sleep(1)

if __name__ == '__main__':
    main()
