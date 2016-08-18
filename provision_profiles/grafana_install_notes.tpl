Congratulations! You've just installed a Grafana server.

To learn more about your how to configure your Grafana, please see the [documentation](https://provisioner.vpetersson.com/docs/roles/grafana/?utm_source=app&utm_medium=install-notes&utm_campaign=provisioner).

# Credentials

## Grafana

User: admin
Password: `{{ grafana_password }}`

## MySQL

User: {{ mysql_grafana_user }}
Database: {{ mysql_grafana_user }}
Password: `{{ mysql_grafana_password  }}`
