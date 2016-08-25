---
layout: page
title: Prometheus
permalink: /docs/roles/prometheus
tags: docker,mysql,prometheus,role
---

* **Name**: Prometheus
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/grafana_install_notes.tpl)
* **Subdomains:** prometheus, prometheus-pushgateway
* **Container link:** Prometheus's [official container](https://hub.docker.com/r/prom/prometheus/)

## What is Prometheus?

"Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud. Since its inception in 2012, many companies and organizations have adopted Prometheus, and the project has a very active developer and user community. It is now a standalone open source project and maintained independently of any company. To emphasize this and clarify the project's governance structure, Prometheus joined the Cloud Native Computing Foundation in 2016 as the second hosted project after Kubernetes."

## Installation Notes

By default, the system will only monitor itself. This isn't very useful. Hence, in order to configure Prometheus by editing `/usr/local/etc/prometheus.yml` on the host VM. You can read more about how to configure Prometheus in the [Getting Started](https://prometheus.io/docs/introduction/getting_started/) documentation.

### Authentication

Since there is no built-in authentication mechanism in the Prometheus, [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication) is used to protect the end points. This is configured for both the main Prometheus and in the Push Gateway.

The credentials are available in the post installation notes.

### Prometheus Push Gateway

While the official recommendation is to use pull, i.e. let the container pull the metric from the remote servers, it is possible to push metrics as well. This is done through the [Push Gateway](https://github.com/prometheus/pushgateway).

To push data to Prometheus, simply configure your client to use https://prometheus-pushgateway.yourdomain.com.

## Related Roles

* [Docker](/docs/roles/docker)
* [Grafana](/docs/roles/grafana)
