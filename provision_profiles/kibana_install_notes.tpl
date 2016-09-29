Congratulations! You've just installed a Kibana server.

To access your installation, point your browser to: [{{ role | regex_replace('_', '-')  }}.{{public_ip}}.nip.io](http://{{ role | regex_replace('_', '-')  }}.{{public_ip}}.nip.io

For more information on how to configure and use your Kibana server, please visit the [documentation page](https://provisioner.vpetersson.com/docs/roles/kibana?utm_source=app&utm_medium=install-notes&utm_campaign=provisioner).

## Credentials

* User: kibana
* Password: `{{ kibana_password }}`
