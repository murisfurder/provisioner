import json
import requests
from lib import ansible_helper
from lib import redis_helper
from time import sleep


def get_etcd_key(size=3):
    """
    Get a key discover key for `etcd`.
    This is used for creating a CoreOS cluster.
    :param size: int
    """
    endpoint = 'https://discovery.etcd.io/new?size={}'.format(size)
    get_key = requests.get(endpoint)
    if not get_key.status_code == 200:
        return False

    return get_key.content


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

    role = data_sanitizer(task, 'role', type(''))
    username = data_sanitizer(task, 'username', type(''))
    password = data_sanitizer(task, 'password', type(''))
    target_ips = data_sanitizer(task, 'target_ips', type([]))

    print 'Got task {} for {}.format(role, target_ips)'

    print 'role: {}'.format(role)
    print 'username: {}'.format(username)
    print 'password: {}'.format(password)
    print 'target_ips: {}'.format(target_ips)

    # Check for mandatory fields for all roles
    if not (username and password and target_ips and role):
        return False

    inventory = ansible_helper.generate_inventory(
        target_ips=target_ips
    )

    if role == 'ping':
        return ansible_helper.ping_vm(
            remote_user=username,
            remote_pass=password,
            inventory=inventory
        )

    if role == 'cloudcompose':
        return ansible_helper.provision_cloudcompose(
            remote_user=username,
            remote_pass=password,
            inventory=inventory,
        )


def main():
    q = redis_helper.pubsub()

    while True:
        task = q.get_message()

        # Filter out initial message by looking for 'name' key
        if task:
            # try:
            json_payload = json.loads(task['data'])
            task_router(json_payload)
            # except:
            #    print 'Unrecognized message:\n{}'.format(task)
        else:
            sleep(1)

if __name__ == '__main__':
    main()
