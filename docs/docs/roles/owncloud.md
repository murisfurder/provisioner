---
layout: page
title: Owncloud
permalink: /docs/roles/owncloud
tags: docker,mysql,role
---

* **Name**: Owncloud
* **Requirement**: Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/owncloud_install_notes.tpl)
* **Container link:** Docker's [official Owncloud container](https://hub.docker.com/_/owncloud/)

## About Owncloud

"ownCloud is an open source, self-hosted file sync and share app platform. Access & sync your files, contacts, calendars & bookmarks across your devices."

## Installation Notes

 * Point your browser to http(s)://owncloud.yourdomain.com
 * Enter a username and password to create your administrator account
 * Click 'Storage & Database'
  * Select 'MySQL/MariaDB'
  * Populate the username, password and database with the information from your post-installation notes.
  * Enter 'mysql' as the Database host
 * Click  Finish Setup

## Technical Details

Your Owncloud server is running inside Docker and the name of the container is 'owncloud'. The container connects to
a MySQL server (or MariaDB to be precise) that is also running inside Docker.

Please note that your data resides outside of Docker in the folder `/usr/local/owncloud`.

## Related Roles

* [Docker](/docs/roles/docker)
* [MySQL](/docs/roles/mysql)
* [Nginx](/docs/roles/nginx)
