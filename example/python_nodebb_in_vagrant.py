#!/usr/bin/env python

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
SECRET = 'yecUcAladLivetnepeecKakicJagcaf3OdkeOfya',


def initiate_nodebb_cluster():

        return create_task(
            ip=NODES[0]['ip'],
            username=NODE_USERNAME,
            password=NODE_PASSWORD,
            role='nodebb',
            extra_vars={
                'init_db': True,
                'secret': SECRET,
            }
        )


def create_nodebb_servers(max_retries=100):
    tasks = []

    for node in NODES:
        tasks.append(create_task(
            ip=node['ip'],
            username=NODE_USERNAME,
            password=NODE_PASSWORD,
            role='nodebb',
            extra_vars={
                'secret': SECRET,
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


def main():
    print 'This requires that you have already executed `python_weave_in_vagrant.py` and `python_mongodb_cluster_in_vagrant`'
#    initiate_nodebb_cluster()
    create_nodebb_servers()

if __name__ == "__main__":
    main()
