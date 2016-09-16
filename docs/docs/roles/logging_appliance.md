---
layout: page
title: Logging Appliance
permalink: /docs/roles/logging-appliance
tags: docker,kibana,elasticsearch,fluentd,logging,meta,role
---

* **Name**: Logging Appliance
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/meta_logging_appliance_install_notes.tpl)

## What is Logging Appliance?
Logging Appliance is a meta package that includes the following three other roles:

* [Elasticsearch](/docs/roles/elasticsearch)
* [Fluentd](/docs/roles/fluentd)
* [Kibana](/docs/roles/kibana)

It does however do slightly more than this, as it also configures them to work together.

This enables you to ship logs directly into Fluentd, which relays the logs to Elasticsearch. You can then use Kibana to browse and query your logs.

## Installation Notes
See the individual roles.

## Related Roles

* [Docker](/docs/roles/docker)
* [MySQL](/docs/roles/mysql)
* [Elasticsearch](/docs/roles/elasticsearch)
* [Fluentd](/docs/roles/fluentd)
* [Kibana](/docs/roles/kibana)
