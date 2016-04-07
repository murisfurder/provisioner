# PostgreSQL

* *Name*: postgres
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 127.0.0.1:5432

Installs the [official PostgreSQL container](https://hub.docker.com/_postgres/).

The persistent data is stored under `/var/lib/postgresql/data` in the VM.

The password for the user 'postgres' can be extracted by running:

    $ sudo docker inspect postgres | grep POSTGRES_PASSWORD

