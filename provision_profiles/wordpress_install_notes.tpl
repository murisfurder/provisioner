Congratulations! You've just installed a WordPress server.

To access your installation, point your browser to: [{{ role }}.{{public_ip}}.nip.io](http://{{ role }}.{{public_ip}}.nip.io

For more information on how to configure and use your WordPress server, please visit the [documentation page](https://provisioner.vpetersson.com/docs/roles/wordpress?utm_source=app&utm_medium=install-notes&utm_campaign=provisioner).

# Credentials

## MySQL

* User: {{ mysql_wordpress_user }}
* Database: {{ mysql_wordpress_user }}
* Password: `{{ mysql_wordpress_password }}`
