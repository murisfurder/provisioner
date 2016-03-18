#!/usr/bin/env python

import python_example

MASTER_IP = '192.168.33.10'
SLAVE_IPS = ['192.168.33.11', '192.168.33.12']
PASSPHRASE = 'WyctorGhadkevlagmarr'
NODE_USERNAME = 'vagrant'
NODE_PASSWORD = 'foobar123'

print 'Master node job:'
print python_example.create_task(
    ip=MASTER_IP,
    username=NODE_USERNAME,
    password=NODE_PASSWORD,
    role='weave',
    extra_vars={
        'is_master': True,
        'passphrase': PASSPHRASE,
    }
)

print 'Slave node jobs:'
for node_ip in SLAVE_IPS:
    print python_example.create_task(
        ip=node_ip,
        username=NODE_USERNAME,
        password=NODE_PASSWORD,
        role='weave',
        extra_vars={
            'is_slave': True,
            'passphrase': PASSPHRASE,
            'master_ip': MASTER_IP,
        }
    )
