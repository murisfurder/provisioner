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
    """
    Generate a strong password.
    Source:
    http://davidsj.co.uk/blog/python-generate-random-password-strings/
    """

    # Alphanumeric + special characters
    chars = string.letters + string.digits

    return ''.join((random.choice(chars)) for x in range(lenght))


def run_module(
    remote_user=None,
    remote_pass=None,
    inventory=None,
    module_name=None,
    become=True,
    module_args='',
):
    """
    The module will return output directly from Ansible.
    Hosts will be divided into 'dark' (failed) and 'connected' (successful).
    You can check the lenght of this to determine the success or
    failure of the run.
    """
    return ansible.runner.Runner(
        remote_user=remote_user,
        remote_pass=remote_pass,
        module_name=module_name,
        module_args=module_args,
        become=become,
        inventory=inventory
    ).run()


def run_playbook(
    remote_user=None,
    remote_pass=None,
    inventory=None,
    playbook_uri=None,
    extra_vars=None,
    only_tags=None,
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
            only_tags=only_tags,
        ).run()
    else:
        print '"{}" is an invalid file.'.format(playbook_uri)


def provision(
        remote_user=None,
        remote_pass=None,
        inventory=None,
        role=None,
        extra_vars={},
        *a,
        **kw
):

    playbook_uri = 'provision_profiles/{}.yml'.format(role)

    if role in [
        'mysql',
        'owncloud',
        'redmine',
        'wordpress',
    ]:
        extra_vars['mysql_root_password'] = generate_password()

        if role == 'owncloud':
            extra_vars['mysql_owncloud_password'] = generate_password()
        if role == 'redmine':
            extra_vars['mysql_redmine_password'] = generate_password()

    if role in ['postgres', 'drupal']:
        extra_vars['postgres_postgres_password'] = generate_password()
        if role == 'drupal':
            extra_vars['postgres_drupal_password'] = generate_password()

    if remote_user and remote_pass and inventory:
        return run_playbook(
            remote_user=remote_user,
            remote_pass=remote_pass,
            inventory=inventory,
            playbook_uri=playbook_uri,
            extra_vars=extra_vars
        )
    else:
        return False


def ping_vm(remote_user, remote_pass, inventory):
    """
    Run Ansible's 'ping' module against the VM.
    Listen for 'pong' in the response from the VM.
    """

    return run_module(
        remote_user=remote_user,
        remote_pass=remote_pass,
        module_name='ping',
        inventory=inventory,
    )


def install_ssh_keys(
    remote_user=None,
    remote_pass=None,
    inventory=None,
    extra_vars=None
):
    """
     Install the SSH key(s) specified in 'ssh-keys' into the
     user account 'ssh-user'.
     'ssh-user' will default to 'remote_user' if absent.
     """

    if not remote_user and remote_pass and inventory and extra_vars:
        print 'Required variable(s) missing.'
        return False

    if 'ssh-user' in extra_vars:
        ssh_user = extra_vars['ssh-user']
    else:
        ssh_user = remote_user

    if 'ssh-keys' in extra_vars:
        ssh_keys = '\n'.join(extra_vars['ssh-keys'])
    else:
        print 'SSH Keys missing. Aborting.'
        return False

    return run_module(
        remote_user=remote_user,
        remote_pass=remote_pass,
        module_name='authorized_key',
        module_args={'user': ssh_user, 'key': ssh_keys},
        inventory=inventory,
    )
