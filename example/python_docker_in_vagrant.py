#!/usr/bin/env python

import settings
from python_example import get_status, create_task
from time import sleep


def create_docker_nodes(max_retries=100):
    tasks = []

    for node in settings.NODES:
        tasks.append(create_task(
            ip=node['ip'],
            username=node['username'],
            password=node['password'],
            role='docker',
        ))

    while max_retries > 0:
        max_retries -= 1

        if len(tasks) < 1:
            return True

        for task in tasks:
            status = get_status(task)
            print 'Task docker ({}) status is {}'.format(
                task,
                status['status']
            )
            if status['status'] in settings.EXIT_STATUS:
                print 'Task weave ({}) exited.'.format(task)
                tasks.remove(task)
        sleep(5)
    else:
        return False


def main():
    create_docker_nodes()

if __name__ == "__main__":
    main()
