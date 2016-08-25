---
layout: page
title: Grafana
permalink: /docs/roles/grafana
tags: docker,mysql,grafana,role
---

* **Name:** Grafana
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/grafana_install_notes.tpl)
* **Subdomain:** grafana
* **Container link:** Grafana's [official container](https://hub.docker.com/r/grafana/grafana/)

## What is Grafana?

"Grafana provides a powerful and elegant way to create, explore, and share dashboards and data with your team and the world."


## Grafana and Prometheus

If you want to use Grafana to graph data from [Prometheus](/docs/roles/grafan), here are the steps to add Prometheus as a data source:

 * Click on the Grafana logo to open the sidebar menu.
 * Click on "Data Sources" in the sidebar.
 * Click on "Add New".
 * Select "Prometheus" as the type.
 * Set the Prometheus server URL to `http://prometheus:9090`
 * Adjust other data source settings as desired (for example, turning the proxy access off).
 * Click "Add" to save the new data source.

For more information, please see the [official documentation](https://prometheus.io/docs/visualization/grafana/)

## Configuration

If you want to make changes to your Grafana configuration, simply update `/usr/local/etc/grafana.ini` on your host server and restart your grafana container (`docker restart grafana`)

## Related Roles

* [Docker](/docs/roles/docker)
* [MySQL](/docs/roles/mysql)
* [Nginx](/docs/roles/nginx)
* [Prometheus](/docs/roles/prometheus)
