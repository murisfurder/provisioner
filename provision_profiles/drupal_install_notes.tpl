Congratulations! You've just installed a Drupal server.

To access your installation, point your browser to: [{{ role | regex_replace('_', '-')  }}.{{public_ip}}.nip.io](http://{{ role | regex_replace('_', '-')  }}.{{public_ip}}.nip.io

For more information on how to configure and use your Drupal server, please visit the [documentation page](https://provisioner.vpetersson.com/docs/roles/drupal?utm_source=app&utm_medium=install-notes&utm_campaign=provisioner).

# Credentials

## MySQL

* User: {{ mysql_drupal_user }}
* Password: `{{ mysql_drupal_password }}`
* Database: {{ mysql_drupal_user }}
