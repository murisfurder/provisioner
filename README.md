# Provisioner

Work in progress!

Simple Ansible based provisioning system for Cloud.net.

## Usage

(With the VMs created matching the data in `create_task.py`)

Spin up the container(s):

```
$ docker-compose build && docker-compose up
```

Create a simple task with [create_task.py](https://github.com/OnApp/provisioner/blob/master/create_task.py):

```
$ docker exec -ti provisioner python create_task.py
```

You will then get something like this in the Docker Compose shell:

```
[...]
prov0 | Got task ping for root@192.168.33.10
prov1 | Got task ping for root@192.168.33.11
prov0 | 192.168.33.10 is running
prov1 | 192.168.33.11 is running
[...]
```

### Detailed use case for CoreOS

(U=User, O=OnApp/Cloud.net, P=Provisioner)

 * [U] User creates a CoreOS cluster in the user interface
 * [O] One Redis task is created for each server in the cluster to the 'prov' channel (three in this case). This task will include:
   * The username for the server ('username')
   * The password for the server ('password')
   * The public IP of the server ('ip')
   * A shared [discovery key](https://discovery.etcd.io/) for etcd ('etcd_discovery')
   * A UNIX timestamp ('timestamp')
 * [O] A Redis key is also set as follows:
  * 'key': ip
  * 'status': 'new'
  * 'ttl': 3600
 * [P] A provisioner worker picks up these tasks (which could be run on three different workers)
 * [P] When a worker picks up the task, it will update the Redis key as follows:
  * 'key': ip
  * 'status': 'provisioning'
  * 'ttl': 3600
 * [P] Upon a successful run, the worker will update the Redis key as follows:
  * 'key': ip
  * 'status': 'done'
  * 'ttl': 3600
* [O] The web interface will poll the status and display a status message to the end user.
