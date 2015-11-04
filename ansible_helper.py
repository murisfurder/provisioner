import ansible.runner
from ansible import utils
from ansible.playbook import PlayBook
from ansible import callbacks
import os


def generate_inventory(uuid=False, public_ip=None):
    inventory = ansible.inventory.Inventory([public_ip])
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
    playbook_path=None,
    playbook_name=None,
    playbook_args='',
):
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    playbook_uri = os.path.join(playbook_path, '{}.yml'.format(playbook_name))

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
