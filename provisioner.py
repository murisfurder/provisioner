import os
import ansible_helper
from pprint import pprint
from time import sleep


PLAYBOOK_PATH = '/Users/mvip/Documents/Business/Viktopia_UK/Clients/OnApp/CloudCompose'

def get_root_password(uuid=False):
    """
    Get the root password for a given machine.
    :param uuid: string
    """
    # @TODO Fetch from upstream
    root_password = 'x+#*Ds,HV7.,'
    return root_password


def get_public_ip(uuid=False):
    """
    Get the public IP of a given machine.
    :param uuid: string
    """
    # @TODO Fetch from upstream
    public_ip = '85.118.238.144'
    return public_ip


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
        return ansible_helper.run_module(
            remote_user=remote_user,
            remote_pass=remote_pass,
            module_name='ping',
            inventory=inventory,
        )

    while not vm_is_online:
        # We run Ansible's 'ping' module and look for the 'pong' response.
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
    inventory = ansible_helper.generate_inventory(public_ip=get_public_ip())

    ping_vm(remote_user, remote_pass, inventory)

    install_cloudcompose = ansible_helper.run_playbook(
        remote_pass=remote_pass,
        inventory=inventory,
        playbook_name='site',
        playbook_path=PLAYBOOK_PATH
    )

    print install_cloudcompose

if __name__ == '__main__':
    main()
