import ansible.runner
from ansible.playbook import PlayBook
import os
from pprint import pprint
from time import sleep


PLAYBOOK_PATH='/Users/mvip/tmp/playbooks'

def get_root_password(uuid=False):
    """
    Get the root password for a given machine.
    :param uuid: string
    """
    root_password = 'x+#*Ds,HV7.,'
    return root_password


def get_public_ip(uuid=False):
    """
    Get the public IP of a given machine.
    :param uuid: string
    """
    public_ip = '85.118.238.144'
    return public_ip


def generate_inventory(uuid=False):
    public_ip = get_public_ip()
    inventory = ansible.inventory.Inventory([public_ip])
    return inventory


def wait_for_vm(uuid=False, max_attempt=10):
    """
    Waits for the VM with `UUID` to become available.
    We use the public IP of a node to determine if it is available or not.
    :param uuid: string
    :param max_attempts: int
    """
    attempt = 0
    while attempt < max_attempt:
        attempt += 1
        public_ip = get_public_ip(uuid)
        if public_ip:
            break
        else:
            sleep(30)


def run_module(
    remote_user='root',
    remote_pass=None,
    inventory=None,
    module_name=None,
    module_args='',
):
    return ansible.runner.Runner(
        remote_user=remote_user,
        remote_pass=remote_pass,
        module_name=module_name,
        module_args=module_args,
        inventory=inventory
    ).run()


def run_playbook(
    remote_user='root',
    remote_pass=None,
    inventory=None,
    playbook_name=None,
    playbook_args='',
):

    playbook_uri = os.path.join(PLAYBOOK_PATH, '{}.yml'.format(playbook_name))

    if not os.path.isfile(playbook_uri):
        return PlayBook(
            playbook=playbook_uri,
            remote_user=remote_user,
            remote_pass=remote_pass,
            inventory=inventory,
        ).run()
    else:
        print '{} is an invalid playbook'.format(playbook_uri)


def wait_for_ip(uuid=False, max_attempt=10):
    """
    Waits for the VM with `UUID` to become available.
    We use the public IP of a node to determine if it is available or not.
    :param uuid: string
    :param max_attempts: int
    """
    attempt = 0
    while attempt < max_attempt:
        attempt += 1
        public_ip = get_public_ip(uuid)
        if public_ip:
            break
        else:
            sleep(30)


def ping_vm(remote_user, remote_pass, inventory):
    vm_is_online = False

    def run_ping():
        return run_module(
            remote_user=remote_user,
            remote_pass=remote_pass,
            module_name='ping',
            inventory=inventory,
        )

    while not vm_is_online:
        if 'pong' in str(run_ping()):
            vm_is_online = True
            print 'VM is online...'
        else:
            print 'Waiting for VM to come online...'
            sleep(10)


def main():
    # Wait for the VM to come online
    wait_for_ip()

    remote_pass = get_root_password()
    remote_user = 'root'
    inventory = generate_inventory()

    ping_vm(remote_user, remote_pass, inventory)

    bootstrap = run_module(
        remote_user=remote_user,
        remote_pass=remote_pass,
        inventory=inventory,
        module_name='apt',
        module_args='name=python-pip state=present update_cache=True cache_valid_time=3600',
    )

    pprint(bootstrap)


if __name__ == '__main__':
    main()
