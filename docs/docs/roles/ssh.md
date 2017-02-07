---
layout: page
title: SSH Key
permalink: /docs/roles/ssh_key
tags: built-in,role
---

* *Name*: ssh
* *Requirement*: Any modern Linux/UNIX operating system.
* *Installation notes*: No

This using the built-in [authorized_key](https://docs.ansible.com/ansible/authorized_key_module.html) module in Ansible. The module is used to install one or many SSH keys.

Additional required keys:

 * `extra_vars['ssh-user']`: The user on the remote system where the key(s) are to be installed.
 * `extra_vars['ssh-keys']`: A list of one or many SSH keys. Must be provided as a list even if there is only one key.

