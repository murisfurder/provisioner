---
layout: page
title: PostgreSQL
permalink: /docs/roles/postgresql
redirect_from:
 - /docs/roles/postgreSQL
 - /docs/roles/postgreql

tags: docker,role
---

* *Name*: postgres
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 127.0.0.1:5432
* *Installation notes*: No

Installs the [official PostgreSQL container](https://hub.docker.com/_postgres/).

The persistent data is stored under `/var/lib/postgresql/data` in the VM.

The password for the user 'postgres' can be extracted by running:

    $ sudo docker inspect postgres | grep POSTGRES_PASSWORD
