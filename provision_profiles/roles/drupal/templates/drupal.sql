CREATE USER drupal ENCRYPTED PASSWORD '{{ postgres_drupal_password }}';
CREATE DATABASE drupal;
GRANT ALL PRIVILEGES ON DATABASE drupal TO drupal;
ALTER DATABASE "drupal" SET bytea_output = 'escape';
