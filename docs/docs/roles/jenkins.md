---
layout: page
title: Jenkins
permalink: /docs/roles/jenkins
tags: docker,role,ci
---

* **Name**: jenkins
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/jenkins_install_notes.tpl)
* **Subdomain:** jenkins
* **Container link:** Docker's [official container](https://hub.docker.com/_/jenkins/)

## What is Jenkins?

"The leading open source automation server, Jenkins provides hundreds of plugins to support building, deploying and automating any project."


## Installation Notes

 * Point your browser to jenkins.yourdomain.com
 * Get the password by running `cat /usr/local/provisioner-data/jenkins/secrets/initialAdminPassword` in your server.
 * Follow the instructions to configure your Jenkins installation and create your administration account

## Technical Details

The data for Jenkins resides in `/usr/local/provisioner-data/jenkins`

## Related Roles

* [Docker](/docs/roles/docker)
* [Nginx](/docs/roles/nginx)
