---
layout: page
title: Server
permalink: /docs/server
tags: docs
---

## Running Provisioner

The easiest way to run Provisioner is to simply use the Docker Compose as mentioned in the [Getting Started](/docs/getting-started)-guide. This will spin up Provisioner for you locally so that you can take it for a spin.

There are however other options that are missing in this setup.

### SSH Keys

Provisioner supports using SSH Keys for authentication with remote systems instead of passwords. This is very handy, as you do not need to send your password to the remote server over the wire with every task creation.

The way this works is by utilizing the environment variable `SSH_PRIVATE_KEYS`. Simply export your private SSH keys with this variable **on all your workers** and you can now run your playbooks without providing a password.

### Default Username

By default, the username used for authenticating with remote servers is 'root'. Depending on your setup, this may or not suite you. Hence, you can simply export the environment variable `REMOTE_USER` to override this.

## Hide Playbooks

If you want to hide some playbooks from the listing, you can set the environment variable `HIDDEN_PLAYBOOKS`. The format of this should be a comma separated list, such as `role1,role2,role3`.

## Production

While you can run Provisioner using the Docker Compose setup, it is recommended that you instead manually deploy Provisioner using your configuration management tool of choice and place it behind a reverse proxy with SSL termination.
