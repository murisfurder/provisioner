---
layout: page
title: MongoDB
permalink: /docs/roles/mongodb
tags: docker,mongodb,role,nosql
---

## Stand-alone

* *Name*: mongodb
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 127.0.0.1:27017
* *Installation notes*: No

Installs the [official MongoDB Docker container](https://hub.docker.com/_/mongo/). MongoDB's persistent data is stored under `/var/lib/mongodb` in the VM.

## Cluster

* *Name*: mongodb
* *Requirement*:
  * Ubuntu 12.04 or later
  * Three VMs
  * Weave module already deployed
* *Exposes ports:* 127.0.0.1:27017

Additional required keys:

 * `extra_vars['is_rs']`: Set to True to initiate replica set configuration of MongoDB.
 * `extra_vars['is_rs_master']`: Set to True to initiate the server as a the master (primary) node.
 * `extra_vars['is_rs_slave']`: Set to True for all slaves (secondaries).
 * `extra_vars['rs_init']`: Set to True to initialize the cluster (must be after the cluster has been fully initiated).

MongoDB can also be deployed in a cluster setup over a Weave network. See [Examples](/docs/examples) for a detailed example of this setup.
