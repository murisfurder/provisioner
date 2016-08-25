---
layout: page
title: Getting Started
permalink: /docs/getting-started
tags: docs
redirect_from:
 - /docs/getting_started
---

To install Provisioner locally, you need Docker, and Docker Compose. Assuming you have both installed, all you need to do is to run:

```
$ git clone https://github.com/OnApp/provisioner.git
$ cd provisioner
$ docker-compose build --pull
$ docker-compose up
```

We can then verify that it works by running:

```
$ curl http://localhost:8080/roles
["docker", "docker_registry", "drupal", "joomla", "letsencrypt", "mongodb", "mysql", "nginx", "owncloud", "postgres", "redis", "redmine", "wordpress"]
```

For more detailed instructions, see the [Server documentation](/docs/server).

## Vagrant Test VM

Sometimes it's handy to have a local Virtual Machine (VM) to test against. For this, we're using Vagrant. There is a Vagrant `Vagrantfile` that defines such test machine for you.

To start the Vagrant VM, run:

```
$ vagrant up
```

Once the containers and the Vagrant VM up and running, you can start creating jobs using something like `curl`:

```
$ curl -H "Content-Type: application/json" \
    -X POST -d '{"role": "ping", "ip": "192.168.33.10", "username": "vagrant", "password": "foobar123"}' \
    http://localhost:8080/job
d7417be8-aab3-435b-8d15-ce71489ca5cd
```

The command will return a UUID. Using this UUID, we can query the status of the job:

```
$ curl http://localhost:8080/job/d7417be8-aab3-435b-8d15-ce71489ca5cd
{"status": "Done", "ip": "192.168.33.10", "attempts": 1, "role": "ping", "timestamp": "1449166675.0"}
```

For more information, please see the [API documentation](/docs/api).
