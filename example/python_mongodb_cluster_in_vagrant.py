#!/usr/bin/env python

from python_example import create_task, get_status
import settings
from time import sleep

# The nodes must be named node0-2 for other roles to work.

NODES = settings.NODES
NODES[0]['master'] = True
NODES[0]['name'] = 'node0'
NODES[1]['master'] = False
NODES[1]['name'] = 'node1'
NODES[2]['master'] = False
NODES[2]['name'] = 'node2'


def create_mongodb_cluster(max_retries=100):
    tasks = []

    for node in NODES:
        tasks.append(create_task(
            ip=node['ip'],
            username=node['username'],
            password=node['password'],
            role='mongodb',
            extra_vars={
                'is_rs': True,
                'is_rs_master': node['master'],
                'is_rs_slave': not node['master'],
                'rs_node_name': node['name'],
            }
        ))

    while max_retries > 0:
        max_retries -= 1

        if len(tasks) < 1:
            return True

        for task in tasks:
            status = get_status(task)
            print 'Task mongodb ({}) status is {}.'.format(
                task,
                status['status']
            )
            if status['status'] in settings.EXIT_STATUS:
                print 'Task mongodb ({}) exited.'.format(task)
                tasks.remove(task)
        sleep(5)
    else:
        return False


def initiate_mongodb_cluster():

        return create_task(
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
    print 'This requires that you have already executed:\n`python_weave_in_vagrant.py`'
    create_mongodb_cluster()
    initiate_mongodb_cluster()

if __name__ == "__main__":
    main()
