# Provisioner

Work in progress!

Simple Ansible based provisioning system for Cloud.net.

## Usage

Spin up the container(s):

```
$ docker build -t cloudnet/prov-worker -f Dockerfile.worker .
$ docker build -t cloudnet/prov-api -f Dockerfile.api .
$ docker-compose up
```

Once the containers are up and running, you can start creating jobs using something like `curl`:

```
$ curl -H "Content-Type: application/json" \
    -X POST -d '{"role": "ping", "ip": "192.168.33.10", "password": "foobar123", "username": "root"}' \
    http://192.168.56.132:8080/submit
d7417be8-aab3-435b-8d15-ce71489ca5cd
```

The command will return a UUID. Using this UUID, we can query the status of the job:

```
$ curl http://192.168.56.132:8080/status/d7417be8-aab3-435b-8d15-ce71489ca5cd
{"status": "Done", "ip": "192.168.33.10", "attempts": 1, "role": "ping", "timestamp": "1449166675.0"}
```

### Provisioning Profiles

The provisioning profile (or role) is set using the `role` key inside the JSON payload.

#### Ping

*Name*: ping
*Requirement*: None

The `ping` profile simply pings the server using Ansible's built-in ping module. Despite the name, this doesn't actually ping (i.e. send an ICMP package), but rather connects to the server over SSH.

#### Docker

*Name*: docker
*Requirement*: Ubuntu 12.04 or later

##### Docker-based profiles

* `mongodb`
* `mysql` (or MariaDB)
* `redis`
* `wordpress`
