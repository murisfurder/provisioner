---
layout: page
title: Docker Registry
permalink: /docs/roles/docker-registry
redirect_from:
 - /docs/roles/docker_registry
tags: docker,role
---

* **Name**: docker_registry
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/docker_registry_install_notes.tpl)
* **Subdomain:** docker-registry
* **Container link:** Dockers's [official container](https://hub.docker.com/_/registry/)


## What is Docker Registry?

"The Registry is a stateless, highly scalable server side application that stores and lets you distribute Docker images. The Registry is open-source, under the permissive Apache license."

## Usage

Your Docker Registry is accessible a docker-registry.yourdomain.com. If you do not have a properly configured DNS name, you can use docker-registry.[your-public-ip].nip.io.

You can read more about how to manage your own Docker Registry [here](https://docs.docker.com/registry/deploying/).

## Configuration

The persistent data is stored under `/usr/local/registry` on the host VM.

## Related Roles

* [Docker](/docs/roles/docker)
