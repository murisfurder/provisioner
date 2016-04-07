# Production Setup

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

## Scaling

To scale the number of workers to four, simply run:

```
$ docker-compose scale worker=4
```
