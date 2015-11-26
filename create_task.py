import time
import json
import settings
from uuid import uuid4
from lib import redis_helper

r = redis_helper.connect()

test_task_1 = {
    'timestamp': str(time.mktime(time.gmtime())),
    'role': 'docker',
    'ip': '192.168.33.10',
    'password': 'foobar123',
    'username': 'root',
    'uuid': str(uuid4())
}

test_task_2 = {
    'timestamp': str(time.mktime(time.gmtime())),
    'role': 'docker',
    'ip': '192.168.33.11',
    'password': 'foobar12',
    'username': 'root',
    'uuid': str(uuid4())
}

print r.publish(settings.REDIS_CHANNEL, json.dumps(test_task_1))
print r.publish(settings.REDIS_CHANNEL, json.dumps(test_task_2))
