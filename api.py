#!/usr/bin/env python

from bottle import request, response, Bottle, run, abort
from lib import redis_helper
from uuid import uuid4
import time
import json


app = Bottle()


@app.post('/job')
def create_job():
    uuid = str(uuid4())
    timestamp = str(time.mktime(time.gmtime()))

    try:
        payload = json.load(request.body)
    except:
        abort(400, 'Invalid JSON payload.')

    ip = payload['ip']
    role = payload['role']
    username = payload['username']
    password = payload['password']

    if 'extra_vars' in payload:
        extra_vars = payload['extra_vars']
    else:
        extra_vars = None

    if not (ip and role and username and password):
        abort(400, 'Missing one of the required arguments.')

    task = redis_helper.add_to_queue({
        'created_at': timestamp,
        'last_update': None,
        'role': role,
        'ip': ip,
        'username': username,
        'password': password,
        'uuid': uuid,
        'attempts': 0,
        'extra_vars': extra_vars,
    })

    if task:
        response.status = 201
        return uuid
    else:
        abort(500, 'Unable to process request')


@app.route('/job/<uuid>')
def get_job_status(uuid):
    if uuid:
        job_query = redis_helper.get_status(uuid)
        if job_query:
            return job_query
        else:
            abort(404, 'Job not found.')
    else:
        print 'No job specified.'
        abort(400, 'No job specified.')


@app.delete('/job/<uuid>')
def abort_job(uuid):
    if uuid:
        abort_task = redis_helper.abort_job(uuid)
        if abort_task:
            response.status = 204
        else:
            abort(500, 'Unable to delete task.')
    else:
        print 'No job specified.'
        abort(400, 'No job specified.')


@app.route('/redis_status')
def get_redis_status():
    return redis_helper.get_redis_status()


@app.route('/')
def root():
    return 'Nothing to see here. Carry on.\n'

run(app, host='0.0.0.0', port=8080, server='gunicorn', workers=4)
