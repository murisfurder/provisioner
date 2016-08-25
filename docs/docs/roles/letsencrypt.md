---
layout: page
title: Let's Encrypt
permalink: /docs/roles/letsencrypt
tags: docker,role
---

* *Name*: nginx
* *Requirement*: Ubuntu 12.04 or later
* *Installation notes*: No

Additional keys:

 * `extra_vars['fqdn']`: Optional. By default the server's hostname is used as the FQDN. You can override this using this key.
 * `extra_vars['email']`: Required. Provide an email address to be assigned to the SSL certificate

This role will automatically issue an SSL certificate for the hostname. This requires that the FQDN points to the IP of the server.

The role will depends on Nginx, and will automatically update Nginx to use the newly issued certificate.
