#!/bin/bash

NGINXCONF=/etc/nginx/conf.d/default.inc
SSLCONF=/etc/nginx/conf.d/ssl-redirect.inc

SUBDOMAINS=(
docker-registry
drupal joomla
grafana
nodebb
owncloud
prometheus
prometheus-pushgateway
redmine
wordpress
)

function generate_cert {
  FQDN="$1"
  EMAIL="$2"
  PARMS=(certonly -n --expand --agree-tos --email $2 --webroot -w /var/www)
  PARMS+=(-d $FQDN)

  for i in ${SUBDOMAINS[*]}; do
    PARMS+=(-d $i.$FQDN)
  done

  /usr/local/sbin/certbot-auto "${PARMS[@]}"
}

function default_stanza {
  echo "location / {"
  echo "    root /var/www;"
  echo "    index index.html index.htm;"
  echo "}"
}

function set_app_as_default {
  echo "location / {"
  echo "    proxy_pass http://$1/;"
  echo "}"
}

function print_help {
  echo 'provfg Help'
  echo
  echo 'To set an app as the default, run:'
  echo '$ provcfg set-default <app>'
  echo 'To revert to the default (no app):'
  echo '$ provcfg set-default none'
  echo 'To generate a Lets Encrypt certificate, run:'
  echo '$ provcfg generate-cert mydomain.com john@doe.com'
  exit 1
}

if [ -z "$1" ]; then
  print_help
fi

if [ "$1" == "set-default" ]; then
  if [ -z "$2" ]; then
    print_help
  fi

  if [ "$2" == "none" ]; then
    echo 'Reverting to default webapp to none.'
    default_stanza > $NGINXCONF
  else
    echo "Setting $2 as the default webapp."
    set_app_as_default "$2" > $NGINXCONF
  fi
elif [ "$1" == "generate-cert" ]; then
  if [ -z "$2" ]; then
    print_help
  elif [ -z "$2" ]; then
    print_help
  fi
  echo "Generating SSL certificate for $1."
  generate_cert "$2" "$3"
else
  print_help
fi

# Refresh SSL
docker exec nginx pkill -HUP -f nginx
