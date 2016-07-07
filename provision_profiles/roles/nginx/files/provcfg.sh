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

function ssl_stanza {
  echo 'if ($scheme = http) {'
  echo '    return 301 https://$server_name$request_uri;'
  echo '}'
}

function print_help {
  echo 'provfg Help'
  echo
  echo 'To set an app as the default, run:'
  echo '$ provcfg set-default <app>'
  echo 'To revert to the default (no app):'
  echo '$ provcfg set-default none'
  echo
  echo 'To redirect all HTTP requests to SSL, run:'
  echo '$ provcfg enable-ssl'
  echo
  echo 'To reset the above command, run:'
  echo '$ provcfg disable-ssl'
  echo
  echo 'To set domain for WordPress, run:'
  echo '$ provcfg set-wp-domain http://yourdomain.com'
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
elif [ "$1" == 'enable-ssl' ]; then
  echo 'Enabling HTTP->HTTPS (SSL) redirect.'
  ssl_stanza > $SSLCONF
elif [ "$1" == 'disable-ssl' ]; then
  echo 'Disabling SSL redirect.'
  rm -f $SSLCONF
elif [ "$1" == 'set-wp-domain' ]; then
  if [ -z "$2" ]; then
    print_help
  fi

  echo "Hard coding WordPress domain to $2"
  docker exec wordpress sed -i '/WP_HOME/ d' wp-config.php
  docker exec wordpress sed -i '/WP_SITEURL/ d' wp-config.php

  echo "define('WP_HOME','$2');" | docker exec -i wordpress tee -a wp-config.php > /dev/null
  echo "define('WP_SITEURL','$2');" | docker exec -i wordpress tee -a wp-config.php > /dev/null

else
  print_help
fi

# Refresh SSL
docker exec nginx pkill -HUP -f nginx
