#!/usr/bin/env python

import requests
import sys
import os
import json
from pprint import pprint
from time import sleep


def get_docker_host():
    """
    Fetch the DOCKER_HOST environment variable and
    parse the IP.
    """

    # raw_dockerhost will return something like:
    # tcp://192.168.56.132:2376
    dockerhost = os.getenv('DOCKER_HOST', None)

    if dockerhost:
        return dockerhost.split(':')[-2].strip('//')
    else:
        print 'Unable to read DOCKER_HOST environment variable.'
        sys.exit(1)


def create_task(ip=None, username=None, password=None, role=None):
    if ip and username and password and role:
        endpoint = 'http://{}:8080/job'.format(get_docker_host())
        payload = {
            'ip': ip,
            'username': username,
            'password': password,
            'role': role
        }
        r = requests.post(endpoint, data=json.dumps(payload))
        if r.status_code == 201:
            return r.content
        else:
            print 'Got error code: {}'.format(r.status_code)
    else:
        print 'Missing arguments.'
        sys.exit(1)


def get_status(uuid):
    if uuid:
        endpoint = 'http://{}:8080/job/{}'.format(get_docker_host(), uuid)
        r = requests.get(endpoint)
        if r.status_code == 200:
            return r.content
        else:
            print 'Unable to get status. Got error code: {}'.format(r.status_code)
    else:
        print 'No UUID specified.'
        sys.exit(1)


def abort_task(uuid):
    if uuid:
        endpoint = 'http://{}:8080/job/{}'.format(get_docker_host(), uuid)
        r = requests.delete(endpoint)
        if r.status_code == 204:
            print 'Successfully aborted task.'
        else:
            print 'Unable to get abort task. Got error code: {}'.format(r.status_code)


def get_redis_status():
    endpoint = 'http://{}:8080/redis_status'.format(get_docker_host())
    r = requests.get(endpoint)
    return r.content


task = create_task(ip='127.0.0.1', username='foobar', password='foobar', role='ping')
sleep(5)
pprint(get_status(task))
abort_task(task)
pprint(get_redis_status())
