---
layout: page
title: Kibana
permalink: /docs/roles/kibana
tags: docker,mysql,kibana,role
---

* **Name**: Kibana
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/kibana_install_notes.tpl)
* **Container link:** Docker's [official Kibana container](https://hub.docker.com/_/kibana/)


## What is Kibana?
"Kibana is an open source data visualization platform that allows you to interact with your data through stunning, powerful graphics. From histograms to geomaps, Kibana brings your data to life with visuals that can be combined into custom dashboards that help you share insights from your data far and wide."

## Installation Notes
No particular installation required. Simply point your browser to http://kibana.yourdomain.com and login with the supplied credentials.

If used with [Fluentd](/docs/roles/fluentd), the data will automatically be populated.

## Related Roles

* [Docker](/docs/roles/docker)
* [MySQL](/docs/roles/mysql)
* [Elasticsearch](/docs/roles/elasticsearch)
* [Fluentd](/docs/roles/fluentd)
