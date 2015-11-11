import ansible_helper
from time import sleep


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


def wait_for_vm(uuid=False, max_attempts=10):
    """
    Waits for the VM with `UUID` to become available.
    We use the public IP of a node to determine if it is available or not.
    :param uuid: string
    :param max_attempts: int
    """
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        public_ip = get_public_ip(uuid)
        if public_ip:
            break
        else:
            sleep(30)


def wait_for_ip(uuid=False, max_attempts=10):
    """
    Waits for the VM with `UUID` to become available.
    We use the public IP of a node to determine if it is available or not.
    :param uuid: string
    :param max_attempts: int
    """
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        public_ip = get_public_ip(uuid)
        if public_ip:
            break
        else:
            sleep(30)


def ping_vm(remote_user, remote_pass, inventory, max_attempts=10):
    """
    Run Ansible's 'ping' module against the VM.
    Listen for 'pong' in the response from the VM.
    """
    vm_is_online = False
    attempts = 0

    def run_ping():
        return ansible_helper.run_module(
            remote_user=remote_user,
            remote_pass=remote_pass,
            module_name='ping',
            inventory=inventory,
        )

    while not vm_is_online and attempts < max_attempts:
        # We run Ansible's 'ping' module and look for the 'pong' response.
        ping = run_ping()
        if 'pong' in str(ping):
            vm_is_online = True
            print 'VM is online...'
        else:
            print ping
            print 'Waiting for VM to come online...'
            attempts += 1
            sleep(10)


def main():
    # Wait for the VM to come online
    wait_for_ip()

    # Define Ansible parameters
    remote_user = 'root'
    remote_pass = get_root_password()
    inventory = ansible_helper.generate_inventory(public_ip=get_public_ip())

    ping_vm(remote_user, remote_pass, inventory)

    ansible_helper.provision_cloudcompose(
        remote_pass=remote_pass,
        inventory=inventory,
    )

if __name__ == '__main__':
    main()
