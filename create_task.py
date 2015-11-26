import time
import json
import settings
from uuid import uuid4
from lib import redis_helper

r = redis_helper.connect()

test_task_0 = {
    'timestamp': str(time.mktime(time.gmtime())),
    'role': 'ping',
    'ip': '192.168.33.10',
    'password': 'foobar123',
    'username': 'root',
    'uuid': str(uuid4())
}

test_task_1 = {
    'timestamp': str(time.mktime(time.gmtime())),
    'role': 'ping',
    'ip': '192.168.33.11',
    'password': 'foobar12',
    'username': 'root',
    'uuid': str(uuid4())
}

test_task_2 = {
    'timestamp': str(time.mktime(time.gmtime())),
    'role': 'docker',
    'ip': '192.168.33.10',
    'password': 'foobar123',
    'username': 'root',
    'uuid': str(uuid4())
}

test_task_3 = {
    'timestamp': str(time.mktime(time.gmtime())),
    'role': 'docker',
    'ip': '192.168.33.11',
    'password': 'foobar12',
    'username': 'root',
    'uuid': str(uuid4())
}

r.publish(settings.REDIS_CHANNEL, json.dumps(test_task_0))
r.publish(settings.REDIS_CHANNEL, json.dumps(test_task_1))
r.publish(settings.REDIS_CHANNEL, json.dumps(test_task_2))
r.publish(settings.REDIS_CHANNEL, json.dumps(test_task_3))
