---
layout: page
title: Use Cases
permalink: /use-cases
tags: navbar
---

## Cloud Service Providers (CSP)

This was the initial use case for Provisioner. [Cloud.net](https://www.cloud.net/) needed a way to configure Virtual Machines (VMs). The problem was that common tools, such as cloud-init were not available. The only method to communicate with the server was over SSH. We could also not make any assumption about the underlaying VM. Since Cloud.net is a federation of many CSPs, the state of these VMs differ and the only thing we could assume was that the VM would be running Ubuntu 12.04 or later.

With this assumption in mind, Provisioner was developed to install common 'apps' (such as WordPress) onto these VMs.

## Continuous Integration (CI) / Continuous Delivery (CD)

Another use case for Provisioner is as part of a CI/CD workflow. Since SSH Keys can be installed inside Provisioner, you do not need to provide your CI server with these keys. Instead, you could simply issue an API call to Provisioner and tell it to execute an Ansible Playbook against either your staging or production environment.
