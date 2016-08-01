# Introduction

Congratulations! You've just installed your own Docker Registry.

# Docker Registry Installation Notes

* Your Docker Registry is now accessible at [docker-registry..yourdomain.com](https://docker-registry.yourdomain.com). If you do not have a properly configured DNS name, you can use [docker-registry.{{ public_ip }}.nip.io](docker-registry.{{ public_ip }}.nip.io)

You can read more about how to manage your own Docker Registry [here](https://docs.docker.com/registry/deploying/).

## Technical Details

* The persistent data is stored under `/usr/local/registry` in the host.
