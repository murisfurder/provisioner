---
layout: page
title: Drupal
permalink: /docs/roles/drupal
tags: docker,mysql,drupal,role
---

* **Name**: Drupal
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/drupal_install_notes.tpl)
* **Container link:** Docker's [official Drupal container](https://hub.docker.com/_/drupal/)


## What is Drupal?
"Drupal is content management software. It's used to make many of the websites and applications you use every day. Drupal has great standard features, like easy content authoring, reliable performance, and excellent security. But what sets it apart is its flexibility; modularity is one of its core principles. Its tools help you build the versatile, structured content that dynamic web experiences need."

## Installation Notes

 * Point your browser to http(s)://drupal.yourdomain.com
 * Select your language
 * Select Standard
 * Select MySQL
  * Enter 'drupal' as the database and username
  * Enter your database password (provided in the installation notes)
 * Select Advanced
  * Enter 'mysql' under host
 * Follow the remaining steps


## Technical Details

Your Drupal server is running inside Docker and the name of the container is 'drupal'. The container connects to a MySQL/MariaDB server that is also running inside Docker.

Please note that the Drupal data resides inside the Docker container. As such, you likely want to use something like [Backup and Migrate](https://www.drupal.org/project/backup_migrate) to make backups of your Drupal installation.

## Related Roles

* [Docker](/docs/roles/docker)
* [MySQL](/docs/roles/mysql)
