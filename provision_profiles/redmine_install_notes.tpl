Congratulations! You've just installed a Redmine server.

To access your installation, point your browser to: [{{ role | regex_replace('_', '-')  }}.{{public_ip}}.nip.io](http://{{ role | regex_replace('_', '-')  }}.{{public_ip}}.nip.io

For more information on how to configure and use your Redmine server, please visit the [documentation page](https://provisioner.vpetersson.com/docs/roles/redmine?utm_source=app&utm_medium=install-notes&utm_campaign=provisioner).

# Credentials

## MySQL

* User: {{ mysql_redmine_user }}
* Database: {{ mysql_redmine_user }}
* Password: `{{ mysql_redmine_password }}`
