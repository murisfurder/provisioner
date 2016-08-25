---
layout: page
title: Nginx
permalink: /docs/roles/nginx
tags: docker,role
---

* *Name*: nginx
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 0.0.0:80, 0.0.0.0:443
* *Installation notes*: No

Additional keys:

 * `extra_vars['fqdn']`: Optional. By default the server's hostname is used as the FQDN in Nginx. You can override this using this key.

Installs the [official Nginx docker container](https://hub.docker.com/_/nginx/).

This role is used as a building block for all web applications. Roles, such as [WordPress](/docs/roles/wordpress), are configured as reverse proxy items inside Nginx.
