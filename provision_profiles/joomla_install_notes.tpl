# Introduction

Congratulations! You've just installed a Joomla! server.

# Joomla! Installation Notes

 * Point your browser to [http://{{ public_ip  }}](http://{{ public_ip }})
 * Fill out the required information to create your administrator account
 * Use the following information in the next step to configure the database:
  * Host Name: `mysql`
  * Username: `{{ mysql_joomla_user }}`
  * Password: `{{ mysql_joomla_password }}`
  * Database Name: `{{ mysql_joomla_user }}`
 * Follow the installation wizard
 * Make sure you click 'Remove Installation Folder' in the last step

# Technical Details

Your Joomla! server is running inside Docker and the name of the container is 'joomla'. The container connects to
a MySQL server that is also running inside Docker.

Please note that the Joomla! data resides inside the Docker container. As such, you likely want to use something like [Akeeba Backup](http://extensions.joomla.org/extension/akeeba-backup) to make backups of your Joomla installation.

Important paths:
 * `/var/lib/mysql` - This is where the MySQL data resides on disk.

To connect to your MySQL instance, use the following command:

```
$ docker run -it --link mysql:mysql --rm mariadb sh -c 'exec mysql -hmysql -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'
```

# Credentials

## MySQL

User: {{ mysql_joomla_user }}
Password: `{{ mysql_joomla_password }}`
Database: {{ mysql_joomla_user }}
