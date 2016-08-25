---
layout: page
title: Redmine
permalink: /docs/roles/redmine
tags: docker,mysql,role
---

* **Name:** Redmine
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/redmine_install_notes.tpl)
* **Subdomain:** redmine
* **Container link:** Docker's [official Redmine container](https://hub.docker.com/_/redmine/)


## What is Redmine?

"Redmine is a flexible project management web application written using Ruby on Rails framework."

## Installation Notes

 * Point your browser to http(s)://redmine.yourdomain.com
 * Press the 'login' link in the upper right-hand corner and login with the credentials 'admin'/'admin'
 * Click 'My Account' in the upper right-hand corner and select 'Change password'
 * Assign a new password to the administrator account

# Technical Details

Uploaded files will reside in `/usr/local/redmine-store/files` outside Docker.

If you want to install plugins to your Redmine, you can place them in `/usr/local/redmine-store/plugins`. Similarly, you can place themes in `/usr/local/redmine-store/themes`.

Redmine's configuration files are located in `/usr/local/redmine-store/config` on the host VM.

## Related Roles

* [Docker](/docs/roles/docker)
* [MySQL](/docs/roles/mysql)
* [Nginx](/docs/roles/nginx)
