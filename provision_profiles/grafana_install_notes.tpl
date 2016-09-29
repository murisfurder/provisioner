Congratulations! You've just installed a Grafana server.

To access your installation, point your browser to: [{{ role }}.{{public_ip}}.nip.io](http://{{ role }}.{{public_ip}}.nip.io

For more information on how to configure and use your Grafana server, please visit the [documentation page](https://provisioner.vpetersson.com/docs/roles/drupal?utm_source=app&utm_medium=install-notes&utm_campaign=provisioner).

# Credentials

## Grafana

* User: admin
* Password: `{{ grafana_password }}`

## MySQL

* User: {{ mysql_grafana_user }}
* Database: {{ mysql_grafana_user }}
* Password: `{{ mysql_grafana_password  }}`
