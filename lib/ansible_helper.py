import ansible.runner
from ansible import utils
from ansible.playbook import PlayBook
from ansible import callbacks
from time import sleep
import os


def generate_inventory(uuid=False, target_ips=None):
    inventory = ansible.inventory.Inventory(target_ips)
    return inventory


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
    playbook_uri=None,
    playbook_args='',
):
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    if os.path.isfile(playbook_uri):
        return PlayBook(
            callbacks=playbook_cb,
            runner_callbacks=runner_cb,
            stats=stats,
            playbook=playbook_uri,
            remote_user=remote_user,
            remote_pass=remote_pass,
            inventory=inventory,
        ).run()
    else:
        print '"{}" is an invalid file.'.format(playbook_uri)


def provision_cloudcompose(
        remote_user=None,
        remote_pass=None,
        inventory=None,
):

    playbook_uri = 'provision_profiles/cloudcompose/site.yml'

    return run_playbook(
        remote_pass=remote_pass,
        inventory=inventory,
        playbook_uri=playbook_uri,
    )


def ping_vm(remote_user, remote_pass, inventory, max_attempts=10):
    """
    Run Ansible's 'ping' module against the VM.
    Listen for 'pong' in the response from the VM.
    """
    vm_is_online = False
    attempts = 0

    def run_ping():
        return run_module(
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
