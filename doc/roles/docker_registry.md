# Docker Registry

* *Name*: docker_registry
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 0.0.0.0:5000

Installs the [official Docker Registry container](https://hub.docker.com/_registry/).

The persistent data is stored under `/usr/local/registry` in the VM.

This setup will by default use unencrypted communication (without authentication). Hence it's only suited for testing.

In order to use the registry, you will need to add the following entry to `/etc/default/docker` (may differ depending on your distribution):

```
DOCKER_OPTS="--insecure-registry a.b.c.d:5000"
```
(Where a.b.c.d is the public IP of your server.)
