#!/usr/bin/env python

from bottle import request
from bottle import Bottle, run
from lib import redis_helper
from uuid import uuid4
import time
import json


app = Bottle()


def create_task(ip=None, role=None, username=None, password=None):
    uuid = str(uuid4())
    timestamp = str(time.mktime(time.gmtime()))
    if (ip and role and username and password):
        redis_helper.add_to_queue({
            'created_at': timestamp,
            'last_update': timestamp,
            'role': role,
            'ip': ip,
            'username': username,
            'password': password,
            'uuid': uuid,
            'attempts': 0,
        })
        return uuid
    else:
        return False


@app.route('/submit', method='POST')
def do_submit():
    payload = json.load(request.body)

    return create_task(
        ip=payload['ip'],
        role=payload['role'],
        username=payload['username'],
        password=payload['password'],
    )


@app.route('/status/<uuid>')
def get_status(uuid):
    if uuid:
        return redis_helper.get_status(uuid)
    else:
        return 'Unable to get status for {}'.format(uuid)


@app.route('/')
def root():
    return 'Nothing to see here. Carry on.\n'

run(app, host='0.0.0.0', port=80, server='gunicorn', workers=4)
