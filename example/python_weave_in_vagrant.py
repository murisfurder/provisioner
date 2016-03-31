#!/usr/bin/env python

from time import sleep
from python_example import get_status, create_task


MASTER_IP = '192.168.33.10'
SLAVE_IPS = ['192.168.33.11', '192.168.33.12']
PASSPHRASE = 'WyctorGhadkevlagmarr'
NODE_USERNAME = 'vagrant'
NODE_PASSWORD = 'foobar123'
EXIT_STATUS = ['Aborted', 'Done', 'Error', 'Failed']


def create_weave_cluster(max_retries=100):
    tasks = []

    tasks.append(create_task(
        ip=MASTER_IP,
        username=NODE_USERNAME,
        password=NODE_PASSWORD,
        role='weave',
        extra_vars={
            'is_master': True,
            'passphrase': PASSPHRASE,
        }
    ))

    for node_ip in SLAVE_IPS:
        tasks.append(create_task(
            ip=node_ip,
            username=NODE_USERNAME,
            password=NODE_PASSWORD,
            role='weave',
            extra_vars={
                'is_slave': True,
                'passphrase': PASSPHRASE,
                'master_ip': MASTER_IP,
            }
        ))

    while max_retries > 0:
        max_retries -= 1

        if len(tasks) < 1:
            return True

        for task in tasks:
            status = get_status(task)
            print 'Task weave ({}) status is {}'.format(task, status['status'])
            if status['status'] in EXIT_STATUS:
                print 'Task weave ({}) exited.'.format(task)
                tasks.remove(task)
        sleep(5)
    else:
        return False


def main():
    create_weave_cluster()

if __name__ == "__main__":
    main()
