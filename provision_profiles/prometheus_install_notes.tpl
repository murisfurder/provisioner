Congratulations! You've just installed a Prometheus server.

To access your installation, point your browser to: [{{ role }}.{{public_ip}}.nip.io](http://{{ role }}.{{public_ip}}.nip.io).

For more information on how to configure and use your Prometheus server, please visit the [documentation page](https://provisioner.vpetersson.com/docs/roles/prometheus?utm_source=app&utm_medium=install-notes&utm_campaign=provisioner).

# Credentials

## Prometheus

* User: prometheus
* Password: `{{ prometheus_password }}`
