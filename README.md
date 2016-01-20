# Provisioner

Work in progress!

Simple Ansible based provisioning system for Cloud.net.

## Usage

Spin up the container(s):

```
$ docker-compose build
$ docker-compose up
```

In the example below, we'll be testing against a Vagrant box configured in `Vagrantfile`. Assuming you have Vagrant up and running, all you need to do is to run:

```
vagrant up
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

For an example Python implementation, please see [python_example.py](https://github.com/OnApp/provisioner/blob/master/example/python_example.py).

### Scaling

To scale the number of workers to four, simply run:

```
$ docker-compose scale worker=4
```

## API Documentation

### Create a job

To create a task, you need to issue a POST against `/job` with the following payload:

```
{
  'role': 'SomeRole',
  'ip': 'TargetIP',
  'username': 'YourUser',
  'password': 'YourPassword'
}
```

If the task was successfully created, you should receive a 201 status code as well as the UUID for the task. The UUID is needed to get the status of the task.

For more information about the possible roles, see [Roles](#Roles).

### Get the status of a job

To get the status of a job, simply issue a GET against `/job/SomeUUID`. You should then get something like this in return (and a 200 status code):

```
{
  "status": "Done",
  "ip": "192.168.33.10",
  "attempts": 1,
  "role": "ping",
  "timestamp": "1449166675.0"
}
```

The possible statuses for a job are:

* Queued
* Provisioning
* Aborted
* Done
* Error
* Queued

### Abort a job

To abort a job, you can issue a DELETE against `/job/SomeUUID`. This should return a 204 status code if successful.

Please note that this will not *stop* a running job, but rather prevent future attempts.

It's also worth noting that deleting jobs is optional. Jobs will normally either complete (`status: Done`) or reach the maximum amount of retries. Redis will then purge these jobs with after 24 hours.

### Get Redis status

To make it easy to check the status of Redis, the output of Redis' `INFO` command has been exposed. You can get this data by issuing a GET to `/redis_status`

## Roles

For all roles, the 'role', 'ip', 'username' and 'password' keys are required.

### Ping

* *Name*: ping
* *Requirement*: None

The `ping` profile simply pings the server using Ansible's built-in ping module. Despite the name, this doesn't actually ping (i.e. send an ICMP package), but rather connects to the server over SSH.

### Docker

* *Name*: docker
* *Requirement*: Ubuntu 12.04 or later

Installs Docker, docker-compose and the Docker Python library on the host.

## MongoDB

* *Name*: mongodb
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 127.0.0.1:27017

Installs the [official MongoDB Docker container](https://hub.docker.com/_/mongo/). MongoDB's persistent data is stored under `/var/lib/mongodb` in the VM.

## MySQL/MariaDB

* *Name*: mysql
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 127.0.0.1:3306

Installs the [official MariaDB docker container](https://hub.docker.com/_/mariadb/). MariaDB is a community-developed fork of MySQL intended to remain free under the GNU GPL.

The persistent data is stored under `/var/lib/mysql` in the VM.

The MySQL/MariaDB root password is generated upon creation and can be obtained by running:

```
$ sudo docker inspect mysql | grep MYSQL_ROOT_PASSWORD
```

## Redis

* *Name*: redis
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 127.0.0.1:6379

Installs the [official Redis Docker container](https://hub.docker.com/_/redis/).

## WordPress

* *Name*: wordpress
* *Requirement*: Ubuntu 12.04 or later
* *Exposes ports:* 127.0.0.1:3306, 0.0.0.0:80

Installs the [official Wordpress Docker container](https://hub.docker.com/_/wordpress/) as well as the [official MariaDB Docker container](https://hub.docker.com/_/mariadb/).

The MariaDB container is using the same playbook as the 'mysql' role.

Please note that upon final provisioning, tbe WordPress installer will be publicaly exposed.

## SSH keys

* *Name*: ssh-keys
* *Requirement*: Should work on any Linux/UNIX style operating system.

Installs one or more SSH keys.

Additional required keys:

 * `extra_vars['ssh-user']`: The user where to which we want to install the SSH key (defaults to username)
 * `extra_vars['ssh-keys']`: A list of one or more SSH keys to install
