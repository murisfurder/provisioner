---
layout: page
title: WordPress
permalink: /docs/roles/wordpress
tags: docker,role,mysql
---

* **Name**: wordpress
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/wordpress_install_notes.tpl)
* **Subdomain:** wordpress
* **Container link:** Docker's [official container](https://hub.docker.com/_/wordpress/)

## What is WordPress?

"WordPress is web software you can use to create a beautiful website, blog, or app. We like to say that WordPress is both free and priceless at the same time."


## Installation Notes

 * Point your browser to wordpress.yourdomain.com
 * Follow the instructions to configure your WordPress site and create your administration account

## Technical Details

All data resides inside the Docker container. As such, you may want to use something like [BackUpWordPress](https://wordpress.org/plugins/backupwordpress/), [VaultPress](https://jetpack.com/support/vaultpress/) or the built-in export tool to make periodic backups of your WordPress installation.

## Related Roles

* [Docker](/docs/roles/docker)
* [MySQL](/docs/roles/mysql)
* [Nginx](/docs/roles/nginx)
