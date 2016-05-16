# Installation

 * Point your browser to http://{{ public_ip }}
 * Select your language
 * Select Standard
 * Select PostgreSQL
  * Enter 'drupal' as the database and username
  * Enter '{{ postgres_drupal_password }}' as the password
 * Select Advanced
  * Enter 'postgres' under host

# Credentials

## PostgreSQL

User: posgres
Password: {{ posgres_postgres_password }}

User: drupal
Password: {{ postgres_drupal_password }}
Database: drupal
