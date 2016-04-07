# Provisioner

**Warning**: Work in progress.

**tl;dr**: Provisioner is a RESTful API for Ansible (or a more primitive version of [Ansible Tower](https://www.ansible.com/tower)).

The tool was developed for [Cloud.net](https://www.cloud.net) to bootstrap remote servers over SSH.

## Usage

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

For an example Python implementation, please see [examples/python_example.py](https://github.com/OnApp/provisioner/blob/master/example/python_example.py).

### Scaling

To scale the number of workers to four, simply run:

```
$ docker-compose scale worker=4
```

### Production use

The above setup is for local and development setups. If you want to use this for a production or stage  environment, the setup differs a little bit.

First, you want to make sure to use properly signed SSL certificates (I'd recommend [Let's Encrypt](https://letsencrypt.org/), which the images already is prepared for. Since the path to the certificate files are hard coded in `docker-compose-prod.yml`, we need to symlink them:

```
$ mkdir -p /etc/ssl/private/
$ ln -s /etc/letsencrypt/live/example.com/fullchain.pem /etc/ssl/private/prov.crt
$ ln -s /etc/letsencrypt/live/example.com/privkey.pem /etc/ssl/private/prov.key
```

In addition to a proper SSL certificate, the production image is also setup to basic auth to keep users out. For this, we leverage the built-in functionality in Nginx. To generate the required files, you need the tool `htpasswd` installed on the server (or locally). These files are bind mounted from the host server. To set this up, run the following commands:

```
$ mkdir -p /etc/nginx
$ htpasswd -c /etc/nginx/htpasswd jdoe
$ curl -o /etc/nginx/auth.conf https://raw.githubusercontent.com/OnApp/provisioner/master/docker/example_nginx_auth.conf
```

Finally, we can start the containers using the following command:
```
$ docker-compose -f docker-compose-prod.yml up -d
```


## More Information

 * [API documentation](doc/api.md)
 * [Roles](doc/roles/)
