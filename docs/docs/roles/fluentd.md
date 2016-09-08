---
layout: page
title: fluentd
permalink: /docs/roles/fluentd
tags: docker,fluentd,elasticsearch,logging,role
---

* **Name**: Fluentd
* **Requirement:** Ubuntu 12.04 or later
* **Installation notes:** [Yes](https://github.com/OnApp/provisioner/blob/master/provision_profiles/fluentd_install_notes.tpl)
* **Container link:** [Container](https://hub.docker.com/r/vpetersson/fluentd-elasticsearch/)

## What is Fluentd?
"Fluentd is an open source data collector, which lets you unify the data collection and consumption for a better use and understanding of data."

## Configure a Client

To log to the central Fluentd server, you need [td-agent](http://www.fluentd.org/download). You will also need the [fluent-plugin-secure-forward](https://github.com/tagomoris/fluent-plugin-secure-forward) plugin installed in order to communicate over HTTPS.

Depending on what you're looking to log, the configuration will vary. You will however need the following stanza in order to ship logs to your Fluentd server:

```
<source>
  @type forward
</source>
<match secure.**>
    @type secure_forward
    shared_key YourSecret
    self_hostname my-fancy-server.local
    enable_strict_verification yes
    secure true
    <server>
      host fluentd.yourdomain.com
      port 24284
    </server>
</match>
```

After you've configured your client and verified that there were no errors in td-agent's logs, you can trigger a message to be sent by running:

```
echo '{"message":"Testing Provisioner"}' | fluent-cat --json secure.test
```

## Technical Details


## Related Roles

* [Docker](/docs/roles/docker)
* [MySQL](/docs/roles/mysql)
* [Kibana]/docs/roles/kibana)
* [Elasticsearch](/docs/roles/elasticsearch)
