---
layout: page
title: GitLab Community Edition (CE)
permalink: /docs/roles/gitlab
tags: docker,role
---

* **Name**: gitlab
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/gitlab_install_notes.tpl)
* **Subdomain:** gitlab
* **Container link:** GitLab's [official container](https://hub.docker.com/r/gitlab/gitlab-ce/)

## What is GitLab?

"Provides Git repository management, code reviews, issue tracking, activity feeds and wikis. GitLab itself is also free software."

## Installation Notes

 * Point your browser to gitlab.yourdomain.com
 * Follow the instructions to configure your GitLab instance and create your administration account

## Technical Details

The GitLab container is running a number of services, such as Redis and PostgreSQL. Hence, it's operating more like a Virtual Machine (VM) than a regular Docker container. Because of this, we're unable to utilize other shared components.

It should also be noted that pushing and pulling to Git repositories over SSH will not work.

Here are the relevant storage paths on the host system:

 * `/usr/local/etc/gitlab`: GitLab's configuration files.
 * `/var/log/gitlab`: GitLab's logs.
 * `/usr/local/gitlab`: GitLab's persistent data storage.


## Related Roles

* [Docker](/docs/roles/docker)
