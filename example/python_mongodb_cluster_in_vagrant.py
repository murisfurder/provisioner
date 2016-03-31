#!/usr/bin/env python

from python_weave_in_vagrant import create_weave_cluster
from python_example import create_task, get_status
from time import sleep


NODES = [
    {'name': 'node0', 'ip': '192.168.33.10', 'master': True},
    {'name': 'node1', 'ip': '192.168.33.11', 'master': False},
    {'name': 'node2', 'ip': '192.168.33.12', 'master': False},
]
NODE_USERNAME = 'vagrant'
NODE_PASSWORD = 'foobar123'
EXIT_STATUS = ['Aborted', 'Done', 'Error', 'Failed']


def create_mongodb_cluster(max_retries=100):
    tasks = []

    for node in NODES:
        tasks.append(create_task(
            ip=node['ip'],
            username=NODE_USERNAME,
            password=NODE_PASSWORD,
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
            print 'Task mongodb ({}) status is {}'.format(task, status['status'])
            if status['status'] in EXIT_STATUS:
                print 'Task mongodb ({}) exited.'.format(task)
                tasks.remove(task)
        sleep(5)
    else:
        return False


def initiate_mongodb_cluster():

        return create_task(
            ip=NODES[0]['ip'],
            username=NODE_USERNAME,
            password=NODE_PASSWORD,
            role='mongodb',
            extra_vars={
                'is_rs': True,
                'rs_init': True,
                'rs_node_name': NODES[0]['name'],
            }
        )


def main():
    create_weave_cluster()
    create_mongodb_cluster()
    initiate_mongodb_cluster()

if __name__ == "__main__":
    main()
