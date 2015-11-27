from lib import ansible_helper
from lib import redis_helper
from time import sleep


def task_router(task):
    """
    Task router for Redis tasks, with sanity check
    """

    def data_sanitizer(data, key, expected_type):
        """
        Sanity check the data against expected data type.
        Returns the value or False.
        """

        if key not in data:
            return False

        # @TODO fix me.
        # if not type(data[key]) is expected_type:
        #    return False

        return data[key]

    def push_status(status=None, ip=None):
        redis_helper.push_status({
            'status': status,
            'ip': ip,
        })

    # Define and lookup the required variables
    role = data_sanitizer(task, 'role', type(''))
    username = data_sanitizer(task, 'username', type(''))
    password = data_sanitizer(task, 'password', type(''))
    target_ip = data_sanitizer(task, 'ip', type(''))

    # Make sure we received all required fields
    if not (username and password and target_ip and role):
        print 'Missing required value'
        return False

    # Give it maximum three attempts
    if 'attempts' in task:
        if task['attempts'] > 2:
            return 'Too many attempts for {}@{}'.format(username, target_ip)
        task['attempts'] += 1
    else:
        task['attempts'] = 1
    attempts = task['attempts']

    print 'Got task {} for {}@{} (attempt {})'.format(
        role,
        username,
        target_ip,
        attempts
    )

    push_status(ip=target_ip, status='provisioning')

    inventory = ansible_helper.generate_inventory(
        target_ip=target_ip
    )

    if role == 'ping':
        run_ping = ansible_helper.ping_vm(
            remote_user=username,
            remote_pass=password,
            inventory=inventory
        )
        if run_ping:
            print '{} is running'.format(target_ip)
            push_status(ip=target_ip, status='done')
        else:
            # @TODO add back to queue.
            pass
    elif role == 'docker':
        run_playbook = ansible_helper.provision_docker(
            remote_user=username,
            remote_pass=password,
            inventory=inventory,
        )
        if (
            run_playbook[target_ip]['unreachable'] == 0 and
            run_playbook[target_ip]['failures'] == 0
        ):
            push_status(ip=target_ip, status='done')
        else:
            redis_helper.add_to_queue(task)
            return 'Failed provisioning {} for {}@{}'.format(
                role,
                username,
                target_ip
            )
    elif role == 'cloudcompose':
        run_playbook = ansible_helper.provision_cloudcompose(
            remote_user=username,
            remote_pass=password,
            inventory=inventory,
        )
        if (
            run_playbook[target_ip]['unreachable'] == 0 and
            run_playbook[target_ip]['failures'] == 0
        ):
            push_status(ip=target_ip, status='done')
        else:
            redis_helper.add_to_queue(task)
            return 'Failed provisioning {} for {}@{}'.format(
                role,
                username,
                target_ip
            )

        print 'Done provisioning {} for {}@{}'.format(
            role,
            username,
            target_ip
        )


def main():
    while True:
        task = redis_helper.pop_from_queue()

        if task:
            task_router(task)
        else:
            sleep(1)

if __name__ == '__main__':
    main()
