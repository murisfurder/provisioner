# Provisioner

Work in progress!

Simple Ansible based provisioning system for Cloud.net.

## Usage

Spin up the container(s):

```
$ docker-compose build && docker-compose up
```

Create a simple task with [create_task.py](https://github.com/OnApp/provisioner/blob/master/create_task.py):

```
$ docker exec -ti provisioner python create_task.py
```

