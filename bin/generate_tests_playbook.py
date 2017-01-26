import os

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
PLAYBOOK_DIR = os.path.join(SCRIPT_PATH, '..', 'provision_profiles')
ROLES_DIR = os.path.join(PLAYBOOK_DIR, 'roles')


def get_roles():
    roles = []
    for folder in os.listdir(ROLES_DIR):
        if os.path.isdir('{}/{}'.format(ROLES_DIR, folder)):

            # Need to disable this role as 'includes' do not
            # work with syntax checks.
            if not folder == 'prometheus_node_exporter':
                roles.append(folder)
    return roles


def build_file(roles):
    playbook = "- name: All roles\n  hosts: all\n  roles:\n"
    for role in roles:
        playbook += "    - {}\n".format(role)
    return playbook


def main():
    roles = get_roles()
    playbook = build_file(roles)
    with open('{}/all.yml'.format(PLAYBOOK_DIR), 'w') as f:
        f.write(playbook)


if __name__ == "__main__":
    main()
