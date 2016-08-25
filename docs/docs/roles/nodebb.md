---
layout: page
title: NodeBB
permalink: /docs/roles/nodebb
tags: docker,mongodb,weave,role
---

* *Name*: nodebb
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 0.0.0.0:4567
* *Requires roles:*
  * Weave
  * MongoDB Cluster
* *Installation notes*: No

## Extra Vars:

* secret: Shared secret for cookies
* rs_servers: Comma separated list of MongoDB servers
* init_db: If set to True, a sample database will be created. The credentials are admin/password. You should **not** use this for anything other than testing.
