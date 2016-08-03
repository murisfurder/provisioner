# Introduction

Congratulations! You've just installed a Drupal server.

# Drupal Installation Notes

 * Point your browser to [https://{{ role }}.yourdomain.com](https://{{ role }}.yourdomain.com)
 * Select your language
 * Select Standard
 * Select MySQL
  * Enter 'drupal' as the database and username
  * Enter `{{ mysql_drupal_password }}` as the password
 * Select Advanced
  * Enter 'mysql' under host
 * Follow the remaining steps


# Technical Details

Your Drupal server is running inside Docker and the name of the container is 'drupal'. The container connects to a MySQL/MariaDB server that is also running inside Docker.

Please note that the Drupal data resides inside the Docker container. As such, you likely want to use something like [Backup and Migrate](https://www.drupal.org/project/backup_migrate) to make backups of your Drupal installation.


Important paths:

* `/var/lib/mysql` - This is where the MySQL data resides on disk.

To connect to your MySQL instance, use the following command:

```
$ docker run -it --link mysql:mysql --rm mariadb sh -c 'exec mysql -hmysql -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'
```

# Credentials

## MySQL

User: {{ mysql_drupal_user }}
Password: `{{ mysql_drupal_password }}`
Database: {{ mysql_drupal_user }}
