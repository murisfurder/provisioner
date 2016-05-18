# Introduction

Congratulations! You've just installed a Drupal server.

# Drupal Installation Notes

 * Point your browser to http://{{ public_ip }}
 * Select your language
 * Select Standard
 * Select PostgreSQL
  * Enter 'drupal' as the database and username
  * Enter `{{ postgres_drupal_password }}` as the password
 * Select Advanced
  * Enter 'postgres' under host
 * Follow the remaining steps


# Technical Details

Your Drupal server is running inside Docker and the name of the container is 'drupal'. The container connects to
a PostgreSQL server that is also running inside Docker.

The runtime environment inside Docker is ephemeral and all persistent storage resides outside of the runtime environment. The two important locations are as follows:

 * `/usr/local/drupal` - This is where the user generated content (themes etc) resides.
 * `/var/lib/postgresql` - This is where the PostgreSQL data resides on disk.

To connect to the PostgreSQL database, use the following command:

```
$ docker exec -ti postgres psql -U postgres
```


# Credentials

## PostgreSQL

User: posgres
Password: `{{ posgres_postgres_password }}`

User: drupal
Password: `{{ postgres_drupal_password }}`
Database: drupal
