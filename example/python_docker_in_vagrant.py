#!/usr/bin/env python

import python_example
from time import sleep

job_id = python_example.create_task(
    ip='192.168.33.10',
    username='vagrant',
    password='foobar123',
    role='docker'
)

finished = False
while not finished:
    exit_status = ['Aborted', 'Done', 'Error']
    status = python_example.get_status(job_id)
    if status['status'] in exit_status:
        DONE = True
        break
    else:
        print status
    sleep(5)
