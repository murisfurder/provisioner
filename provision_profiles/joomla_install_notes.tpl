Congratulations! You've just installed a Joomla! server.

To access your installation, point your browser to: [{{ role }}.{{public_ip}}.nip.io](http://{{ role }}.{{public_ip}}.nip.io).

For more information on how to configure and use your Joomla! server, please visit the [documentation page](https://provisioner.vpetersson.com/docs/roles/joomla?utm_source=app&utm_medium=install-notes&utm_campaign=provisioner).

# Credentials

## MySQL

* User: {{ mysql_joomla_user }}
* Password: `{{ mysql_joomla_password }}`
* Database: {{ mysql_joomla_user }}
