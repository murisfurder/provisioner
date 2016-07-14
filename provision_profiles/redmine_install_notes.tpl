# Introduction

Congratulations! You've just installed a Redmine server.

# Redmine Installation Notes

 * Point your browser to [https://{{ role }}.yourdomain.com](https://{{ role }}.yourdomain.com)
 * Press the 'login' link in the upper right-hand corner and login with the credentials 'admin'/'admin'
 * Click 'My Account' in the upper right-hand corner and select 'Change password'
 * Assign a new password to the administrator account

# Technical Details

Your Redmine server is running inside Docker and the name of the container is 'redmine'. The container connects to a MySQL server (or MariaDB to be precise) that is also running inside Docker.

Uploaded files will reside in `/usr/local/redmine-store/files` outside Docker.

If you want to install plugins to your Redmine, you can place them in `/usr/local/redmine-store/plugins`. Similarly, you can place themes in `/usr/local/redmine-store/themes`.

To connect to your MySQL instance, use the following command:

```
$ docker run -it --link mysql:mysql --rm mariadb sh -c 'exec mysql -hmysql -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'
```

# Credentials

## MySQL

User: {{ mysql_redmine_user }}
Database: {{ mysql_redmine_user }}
Password: `{{ mysql_redmine_password }}`
