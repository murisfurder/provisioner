# Introduction

Congratulations! You've just installed an Owncloud server.

# Owncloud Installation Notes

 * Point your browser to [https://{{ role }}.yourdomain.com](https://{{ role }}.yourdomain.com)
 * Enter a username and password to create your administrator account
 * Click 'Storage & Database'
  * Select 'MySQL/MariaDB'
  * Enter '{{ mysql_owncloud_user }}' as Database user
  * Enter '{{ mysql_owncloud_password  }}' as the password
  * Enter '{{ mysql_owncloud_user }}' as the Database name
  * Enter 'mysql' as the Database host
 * Click  Finish Setup

# Technical Details

Your Owncloud server is running inside Docker and the name of the container is 'owncloud'. The container connects to
a MySQL server (or MariaDB to be precise) that is also running inside Docker.

Your data resides outside of Docker in the folder `/usr/local/owncloud`.

To connect to your MySQL instance, use the following command:

```
$ docker run -it --link mysql:mysql --rm mariadb sh -c 'exec mysql -hmysql -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'
```

# Credentials

## MySQL

Database: {{ mysql_owncloud_user }}
User: {{ mysql_owncloud_user }}
Password: {{ mysql_owncloud_password }}
