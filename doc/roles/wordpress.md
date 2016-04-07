# WordPress

* *Name*: wordpress
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 127.0.0.1:3306, 0.0.0.0:80

Installs the [official Wordpress Docker container](https://hub.docker.com/_/wordpress/) as well as the [official MariaDB Docker container](https://hub.docker.com/_/mariadb/).

The MariaDB container is using the same playbook as the 'mysql' role.

Please note that upon final provisioning, the WordPress installer will be publicly exposed.

