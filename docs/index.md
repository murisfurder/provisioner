---
layout: page
title: Home
permalink: /
tags: home
---

### tl;dr

Provisioner is a simple minimal wrapper that exposes Ansible over a RESTful API. It's similar in some ways to Ansible's commercial [Tower](https://www.ansible.com/tower) service.

Want to give it a spin? Check out the [Getting Started](/docs/getting-started) guide.

### Demo

<script type="text/javascript" src="https://asciinema.org/a/9wa53j3ppvejqcc1ci2w6u4dg.js" id="asciicast-9wa53j3ppvejqcc1ci2w6u4dg" async></script>

Here's what's going on in the demo:

 * Provisioner is started via `docker-compose`
 * We check on the Vagrant boxes (the targets)
 * Using our python library, we create a [ping](/docs/roles/ping) job
 * We verify that the ping job was executed in the Docker logs
 * We query the status from the task using the API

### About

The tool was developed for [Cloud.net](https://www.cloud.net) to bootstrap remote servers over SSH.

Provisioner also comes with a large number of pre-configured 'apps' (referred to as 'roles'). These apps include popular tools, such as [WordPress](/docs/roles/wordpress), [Drupal](/docs/roles/drupal) or [PostgreSQL](/docs/roles/postgresql).

Most of these apps are deployed inside Docker containers on the host, and have been configured such that you can deploy multiple apps on a single server. For instance, you can have *https://drupal.mydomain.com* and *https://wordpress.mydomain.com* served from the same server.

Also, thanks to [Let's Encrypt](https://letsencrypt.org/), we're able to automatically create valid SSL certificates on the remote host.
