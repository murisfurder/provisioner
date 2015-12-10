import ansible.runner
from ansible import utils
from ansible.playbook import PlayBook
from ansible import callbacks
import os
import random
import string


def generate_inventory(uuid=False, target_ip=None):
    inventory = ansible.inventory.Inventory([target_ip])
    return inventory


def generate_password(lenght=20):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(lenght))


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
    extra_vars=None,
    playbook_args='',
):
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    runner_cb = callbacks.PlaybookRunnerCallbacks(
        stats,
        verbose=utils.VERBOSITY
    )

    if os.path.isfile(playbook_uri):
        return PlayBook(
            callbacks=playbook_cb,
            runner_callbacks=runner_cb,
            stats=stats,
            playbook=playbook_uri,
            remote_user=remote_user,
            remote_pass=remote_pass,
            inventory=inventory,
            extra_vars=extra_vars,
        ).run()
    else:
        print '"{}" is an invalid file.'.format(playbook_uri)


def provision_cloudcompose(
        remote_user=None,
        remote_pass=None,
        inventory=None,
):

    if not ping_vm(remote_user, remote_pass, inventory, max_attempts=10):
        return False

    playbook_uri = 'provision_profiles/cloudcompose/site.yml'

    return run_playbook(
        remote_pass=remote_pass,
        inventory=inventory,
        playbook_uri=playbook_uri,
    )


def provision_docker(
        remote_user=None,
        remote_pass=None,
        inventory=None,
):

    playbook_uri = 'provision_profiles/docker/site.yml'

    return run_playbook(
        remote_pass=remote_pass,
        inventory=inventory,
        playbook_uri=playbook_uri,
    )


def provision_wordpress(
        remote_user=None,
        remote_pass=None,
        inventory=None,
):

    playbook_uri = 'provision_profiles/wordpress/site.yml'

    return run_playbook(
        remote_pass=remote_pass,
        inventory=inventory,
        playbook_uri=playbook_uri,
        extra_vars={
            'mysql_root_password': generate_password(),
        }
    )


def ping_vm(remote_user, remote_pass, inventory):
    """
    Run Ansible's 'ping' module against the VM.
    Listen for 'pong' in the response from the VM.
    """

    ping = run_module(
        remote_user=remote_user,
        remote_pass=remote_pass,
        module_name='ping',
        inventory=inventory,
    )

    # We run Ansible's 'ping' module and look for the 'pong' response.
    if 'pong' in str(ping):
        return True
    else:
        return False
