# Introduction

Congratulations! You've just installed your own Docker Registry.

# Docker Registry Installation Notes

* The persistent data is stored under `/usr/local/registry` in the host.
* This setup will by default use unencrypted communication (without authentication). Hence it's only suited for testing.

## Technical Details

In order to use the registry, you will need to add the following entry to `/etc/default/docker` (may differ depending on your distribution):

```
DOCKER_OPTS="--insecure-registry a.b.c.d:5000"
```
