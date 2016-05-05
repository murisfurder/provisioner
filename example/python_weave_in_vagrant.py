#!/usr/bin/env python

import settings
from time import sleep
from python_example import get_status, create_task


MASTER = settings.NODES[0]
SLAVES = settings.NODES[1:]
PASSPHRASE = 'WyctorGhadkevlagmarr'


def create_weave_cluster(max_retries=100):
    tasks = []

    tasks.append(create_task(
        ip=MASTER['ip'],
        username=MASTER['username'],
        password=MASTER['password'],
        role='weave',
        extra_vars={
            'is_master': True,
            'passphrase': PASSPHRASE,
        }
    ))

    for node in SLAVES:
        tasks.append(create_task(
            ip=node['ip'],
            username=node['username'],
            password=node['password'],
            role='weave',
            extra_vars={
                'is_slave': True,
                'passphrase': PASSPHRASE,
                'master_ip': MASTER['ip'],
            }
        ))

    while max_retries > 0:
        max_retries -= 1

        if len(tasks) < 1:
            return True

        for task in tasks:
            status = get_status(task)
            print 'Task weave ({}) status is {}.'.format(task, status['status'])
            if status['status'] in settings.EXIT_STATUS:
                print 'Task weave ({}) exited.'.format(task)
                tasks.remove(task)
        sleep(5)
    else:
        return False


def main():
    create_weave_cluster()

if __name__ == "__main__":
    main()
