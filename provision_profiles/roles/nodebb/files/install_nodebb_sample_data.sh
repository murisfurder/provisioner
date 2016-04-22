#!/bin/bash

if [ ! -f /root/nodebb_sample_install ]; then
    /usr/local/bin/docker-weave-run --rm mongo bash -c "\
      apt-get -q update && \
      apt-get -q install -y curl && \
      curl -o /nodebb_sample.tgz https://raw.githubusercontent.com/vpetersson/docker-nodebb/master/sample/nodebb_sample.tgz && \
      tar xvfz /nodebb_sample.tgz -C /tmp && \
      mongorestore --host {{ rs_name }}/{{ rs_servers }} /tmp/dump" > /root/nodebb_sample_install
fi
