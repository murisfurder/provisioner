import json
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

    # Ensure that data is proper JSON
    try:
        json_payload = json.loads(task['data'])
    except:
        print 'Unrecognized message:\n{}'.format(task)
        return

    # Define and lookup the required variables
    role = data_sanitizer(json_payload, 'role', type(''))
    uuid = data_sanitizer(json_payload, 'uuid', type(''))
    username = data_sanitizer(json_payload, 'username', type(''))
    password = data_sanitizer(json_payload, 'password', type(''))
    target_ip = data_sanitizer(json_payload, 'ip', type(''))

    # Make sure we received all required fields
    if not (username and password and target_ip and role):
        print 'Missing required value'
        return False

    lock = redis_helper.get_lock(uuid)
    if lock.acquire(blocking=False):
        print 'Got task {} for {}@{}'.format(role, username, target_ip)
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
            return ansible_helper.provision_docker(
                remote_user=username,
                remote_pass=password,
                inventory=inventory,
            )
        elif role == 'cloudcompose':
            return ansible_helper.provision_cloudcompose(
                remote_user=username,
                remote_pass=password,
                inventory=inventory,
            )

        print 'Done provisioning {} for {}@{}'.format(
            role,
            username,
            target_ip
        )


def main():
    q = redis_helper.pubsub()

    while True:
        task = q.get_message()

        # Filter out initial message by looking for 'name' key
        if task:
            task_router(task)
        else:
            sleep(1)

if __name__ == '__main__':
    main()
