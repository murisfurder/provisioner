#!/bin/bash

NGINXCONF=/etc/nginx/conf.d/default.inc
SSLCONF=/etc/nginx/conf.d/ssl-redirect.inc

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
else
  print_help
fi

# Refresh SSL
docker exec nginx pkill -HUP -f nginx
