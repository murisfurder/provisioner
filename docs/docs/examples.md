---
layout: page
title: Examples
permalink: /docs/examples
tags: docs
---

## Install the Python library

To simplify the code examples, we'll use our [Python library](https://github.com/OnApp/py-provisioner). You can install this by running:

```
$ pip install provisioner
```

## Provision SSH keys

Let's start with something simple and use the role [ssh-key](/docs/roles/ssh_key) to install SSH keys to a remote VM.

First, we import the module and set the key.

```
>>> import provisioner
>>> SSH_KEY = 'ssh-rsa AAAAB3N[...]'
```

Next, we use the built-in mechanism for detecting a local provisioner instance. You can also hard code this value. The format should we a complete URL, such as *https://prov.example.com* or *http://localhost:8080*.

```
>>> PROV_URL = provisioner.get_provisioner_url()
```

As our target box, let's use one of our [Vagrant boxes](https://github.com/OnApp/provisioner/blob/master/Vagrantfile) that are part of the installation:

```
>>> TARGET_BOX = provisioner.SAMPLE_NODES[0]
```

Finally, let's create the actual job.

```
>>> provisioner.create_job(
    provisioner_url=PROV_URL,
    ip=TARGET_BOX['ip'],
    username=TARGET_BOX['username'],
    password=TARGET_BOX['password'],
    role='ssh-keys',
    extra_vars={
        'ssh-user': 'vagrant',
        'ssh-keys': [SSH_KEY],
    }
)
{'message': '0258fc79-e3ae-400e-9c7b-8007296b5088', 'http_status': 201}
```

This is the Job ID. We can then check on the status on this job by running by calling on `get_status`:

```
>>> provisioner.get_status(
    provisioner_url=PROV_URL,
    uuid='0258fc79-e3ae-400e-9c7b-8007296b5088',
)
{'message': {u'status': u'Queued', u'ip': u'192.168.33.10', u'install_notes': u'', u'attempts': 0, u'role': u'ssh-keys', u'timestamp': u'1470175672.0', u'msg': []}, 'http_status': 200}
```

Once the job has been picked up and completed, you'll get something like this:

```
>>> provisioner.get_status(
    provisioner_url=PROV_URL,
    uuid='0258fc79-e3ae-400e-9c7b-8007296b5088',
)
{'http_status': 200,
 'message': {u'attempts': 1,
  u'install_notes': u'No installation notes available.',
  u'ip': u'192.168.33.10',
  u'msg': [],
  u'role': u'ssh-keys',
  u'status': u'Done',
  u'timestamp': u'1470184959.0'}}
```

## Provision a Weave cluster

While it's handy to simply provision a [role](/docs/roles/) on a single host, Provisioner can do more fancy things. In the code snippet below, we will setup a [Weave](/docs/roles/weave) cluster, which is an overlay network. This allows you to create a private (encrypted) network that ties together remote servers. This is very useful if you're working with cloud providers that do not offer virtual networks, or if you want to bridge servers in different data centers.

The example will use the three Vagrant VMs as we used above. We will also define a shared `PASSPHRASE` that is used by Weave to setup the shared network.

```
#!/usr/bin/env python

import provisioner
from time import sleep

MASTER = provisioner.SAMPLE_NODES[0]
SLAVES = provisioner.SAMPLE_NODES[1:]
PASSPHRASE = 'MySuperSecret'
PROV_URL = provisioner.get_provisioner_url()


def create_weave_cluster(max_retries=100):
    jobs = []
    role = 'weave'

    r = provisioner.create_job(
        provisioner_url=PROV_URL,
        ip=MASTER['ip'],
        username=MASTER['username'],
        password=MASTER['password'],
        role=role,
        extra_vars={
            'is_master': True,
            'passphrase': PASSPHRASE,
        }
    )
    if r['http_status'] == 201:
        jobs.append(r['message'])
    else:
        print('Failed to add master job.')

    for node in SLAVES:
        r = provisioner.create_job(
            provisioner_url=PROV_URL,
            ip=node['ip'],
            username=node['username'],
            password=node['password'],
            role=role,
            extra_vars={
                'is_slave': True,
                'passphrase': PASSPHRASE,
                'master_ip': MASTER['ip'],
            }
        )
        if r['http_status'] == 201:
            jobs.append(r['message'])
        else:
            print('Failed to add slave {} job.'.format(node['ip']))

    while max_retries > 0:
        max_retries -= 1

        if len(jobs) < 1:
            return True

        for job in jobs:
            status = provisioner.get_status(
                provisioner_url=PROV_URL,
                uuid=job,
            )

            if status['http_status'] == 200:
                print('Job {} ({}) status is {}.'.format(
                    role,
                    job,
                    status['message']['status'],
                ))

                if status['message']['status'] in provisioner.EXIT_STATUS:
                    jobs.remove(job)
            else:
                print('Failed to get status for job {}.'.format(job))
        sleep(5)
    else:
        return False


def main():
    create_weave_cluster()

if __name__ == "__main__":
    main()
```

## Provision MongoDB on top of Weave

Once we have provisioned Weave successfully across our cluster, we can deploy something like [MongoDB](/docs/roles/mongodb) on top of it.

Since the components are designed to play together, we can simply build on top of what we already have.

```
#!/usr/bin/env python

import provisioner
from time import sleep

PROV_URL = provisioner.get_provisioner_url()

# The nodes must be named node0-2 for other roles to work.
NODES = provisioner.SAMPLE_NODES
NODES[0]['master'] = True
NODES[0]['name'] = 'node0'
NODES[1]['master'] = False
NODES[1]['name'] = 'node1'
NODES[2]['master'] = False
NODES[2]['name'] = 'node2'


def create_mongodb_cluster(max_retries=100):
    jobs = []
    role = 'mongodb'

    for node in NODES:
        r = provisioner.create_job(
            provisioner_url=PROV_URL,
            ip=node['ip'],
            username=node['username'],
            password=node['password'],
            role=role,
            extra_vars={
                'is_rs': True,
                'is_rs_master': node['master'],
                'is_rs_slave': not node['master'],
                'rs_node_name': node['name'],
            }
        )
        if r['http_status'] == 201:
            jobs.append(r['message'])
        else:
            print('Failed to create job for {}.'.format(node['ip']))

    while max_retries > 0:
        max_retries -= 1

        if len(jobs) < 1:
            return True

        for job in jobs:
            status = provisioner.get_status(
                provisioner_url=PROV_URL,
                uuid=job
            )

            if status['http_status'] == 200:
                print('Job {} ({}) status is {}.'.format(
                    role,
                    job,
                    status['message']['status'],
                ))

                if status['message']['status'] in provisioner.EXIT_STATUS:
                    jobs.remove(job)
            else:
                print('Failed to get status for job {}.'.format(job))
        sleep(5)
    else:
        return False


def initiate_mongodb_cluster():

        return provisioner.create_job(
            provisioner_url=PROV_URL,
            ip=NODES[0]['ip'],
            username=NODES[0]['username'],
            password=NODES[0]['password'],
            role='mongodb',
            extra_vars={
                'is_rs': True,
                'rs_init': True,
                'rs_node_name': NODES[0]['name'],
            }
        )


def main():
    create_mongodb_cluster()
    initiate_mongodb_cluster()

if __name__ == "__main__":
    main()
```

