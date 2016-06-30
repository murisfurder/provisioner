# Introduction

Congratulations! You've just installed a WordPress server.

# WordPress Installation Notes

 * Point your browser to [http://{{ public_ip  }}](http://{{ public_ip }})
 * Follow the instructions to configure your WordPress site and create your administration account

# Technical Details

Your WordPress server is running inside Docker and the name of the container is 'wordpress'. The container connects to
a MySQL server (or MariaDB to be precise) that is also running inside Docker.

All data resides inside the Docker container. As such, you may want to use something like [BackUpWordPress](https://wordpress.org/plugins/backupwordpress/), [VaultPress](https://jetpack.com/support/vaultpress/) or the built-in export tool to make periodic backups of your WordPress installation.

To connect to your MySQL instance, use the following command:

```
$ docker run -it --link mysql:mysql --rm mariadb sh -c 'exec mysql -hmysql -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'
```

# Credentials

## MySQL

User: wordpress
Database: wordpress
Password: `{{ mysql_wordpress_password  }}`
