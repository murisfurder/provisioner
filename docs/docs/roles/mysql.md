---
layout: page
title: MySQL/MariaDB
permalink: /docs/roles/mysql
tags: docker,mysql,mariadb,role
---

* *Name*: mysql
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 127.0.0.1:3306
* *Installation notes*: No

Installs the [official MariaDB docker container](https://hub.docker.com/_/mariadb/). MariaDB is a community-developed fork of MySQL intended to remain free under the GNU GPL.

The persistent data is stored under `/var/lib/mysql` in the VM.

The MySQL/MariaDB root password is generated upon creation and can be obtained by running:

```
$ sudo docker inspect mysql | grep MYSQL_ROOT_PASSWORD
```
