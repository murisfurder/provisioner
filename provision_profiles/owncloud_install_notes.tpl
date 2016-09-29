Congratulations! You've just installed an Owncloud server.

To access your installation, point your browser to: [{{ role | regex_replace('_', '-')  }}.{{public_ip}}.nip.io](http://{{ role | regex_replace('_', '-')  }}.{{public_ip}}.nip.io

For more information on how to configure and use your Owncloud server, please visit the [documentation page](https://provisioner.vpetersson.com/docs/roles/owncloud?utm_source=app&utm_medium=install-notes&utm_campaign=provisioner).

# Credentials

## MySQL

* Database: {{ mysql_owncloud_user }}
* User: {{ mysql_owncloud_user }}
* Password: {{ mysql_owncloud_password }}
