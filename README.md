# Provisioner

**Warning**: Work in progress.

**tl;dr**: Provisioner is a RESTful API for Ansible (or a more primitive version of [Ansible Tower](https://www.ansible.com/tower)).

The tool was developed for [Cloud.net](https://www.cloud.net) to bootstrap remote servers over SSH.


## Demo

[![asciicast](https://asciinema.org/a/1k90lebjne0j0fk5shuqb9nxm.png)](https://asciinema.org/a/1k90lebjne0j0fk5shuqb9nxm)

A demo of provisioner and the [python_mongodb_cluster_in_vagrant.py](/example/python_mongodb_cluster_in_vagrant.py) example targeting three local Vagrant VMs.

What this does is to:

 * Create a Weave network (Role: [Weave](doc/roles/weave.md))
 * Create a MongoDB ReplicaSet over the Weave network (Role: [MongoDB](doc/roles/mongodb.md))

## Development/local setup

Spin up the container(s):

```
$ docker-compose build --pull
$ docker-compose up
```

In the example below, we'll be testing against a Vagrant box configured in `Vagrantfile`. Assuming you have Vagrant up and running, all you need to do is to run:

```
$ vagrant up
```

Once the containers and the Vagrant VM up and running, you can start creating jobs using something like `curl`:

```
$ curl -H "Content-Type: application/json" \
    -X POST -d '{"role": "ping", "ip": "192.168.33.10", "username": "vagrant", "password": "foobar123"}' \
    http://192.168.56.132:8080/job
d7417be8-aab3-435b-8d15-ce71489ca5cd
```

The command will return a UUID. Using this UUID, we can query the status of the job:

```
$ curl http://192.168.56.132:8080/job/d7417be8-aab3-435b-8d15-ce71489ca5cd
{"status": "Done", "ip": "192.168.33.10", "attempts": 1, "role": "ping", "timestamp": "1449166675.0"}
```

For an example Python implementation, please see [python_example.py](example/python_example.py).

**Do not use this setup in production**, instead please see [production setup](doc/production_setup.md).

## More Information

 * [API documentation](doc/api.md)
 * [Roles](doc/roles/)
