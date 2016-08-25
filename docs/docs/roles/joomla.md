---
layout: page
title: Joomla!
permalink: /docs/roles/joomla
tags: docker,drupal,role
---

* **Name:** Joomla
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/joomla_install_notes.tpl)
* **Subdomain:** joomla
* **Container link:** Docker's [official Joomla! container](https://hub.docker.com/_/joomla/)

## What is Joomla?

"Joomla! is an award-winning content management system (CMS), which enables you to build Web sites and powerful online applications. Many aspects, including its ease-of-use and extensibility, have made Joomla! the most popular Web site software available. Best of all, Joomla is an open source solution that is freely available to everyone."

## Technical Details

Please note that the Joomla! data resides inside the Docker container. As such, you likely want to use something like [Akeeba Backup](http://extensions.joomla.org/extension/akeeba-backup) to make backups of your Joomla installation.

## Related Roles

* [Docker](/docs/roles/docker)
* [MySQL](/docs/roles/mysql)
* [Nginx](/docs/roles/nginx)
