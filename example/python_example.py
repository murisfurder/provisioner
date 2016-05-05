#!/usr/bin/env python

import requests
import sys
import os
import json


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


def create_task(
    ip=None,
    username=None,
    password=None,
    role=None,
    extra_vars=None,
    only_tags=None
):
    if ip and username and password and role:
        endpoint = 'http://{}:8080/job'.format(get_docker_host())
        payload = {
            'ip': ip,
            'username': username,
            'password': password,
            'role': role,
            'extra_vars': extra_vars,
            'only_tags': only_tags,
        }
        r = requests.post(endpoint, data=json.dumps(payload))
        if r.status_code == 201:
            return r.content
        else:
            print 'Got error code: {}'.format(r.status_code)
            print 'Error message:\n{}'.format(r.content)
    else:
        print 'Missing arguments.'
        sys.exit(1)


def get_status(uuid):
    if uuid:
        endpoint = 'http://{}:8080/job/{}'.format(get_docker_host(), uuid)
        r = requests.get(endpoint)
        if r.status_code == 200:
            return json.loads(r.content)
        else:
            return {'status': 'Unable to get status'}
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
            print 'Unable to get abort task. Got error code: {}'.format(
                r.status_code
            )


def install_ssh_keys(
    ip=None,
    username=None,
    password=None,
    role=None,
    ssh_user=None,
    ssh_keys=None
):
    return create_task(
        ip=ip,
        username=username,
        password=password,
        role='ssh-keys',
        extra_vars={
            'ssh-user': ssh_user,
            'ssh-keys': ssh_keys,
        }
    )


def get_redis_status():
    endpoint = 'http://{}:8080/redis_status'.format(get_docker_host())
    r = requests.get(endpoint)
    return r.content
