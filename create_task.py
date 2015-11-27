import time
from uuid import uuid4
from lib import redis_helper

redis_helper.add_to_queue({
    'timestamp': str(time.mktime(time.gmtime())),
    'role': 'ping',
    'ip': '192.168.33.10',
    'password': 'foobar123',
    'username': 'root',
    'uuid': str(uuid4())
})

redis_helper.add_to_queue({
    'timestamp': str(time.mktime(time.gmtime())),
    'role': 'ping',
    'ip': '192.168.33.11',
    'password': 'foobar12',
    'username': 'root',
    'uuid': str(uuid4())
})

redis_helper.add_to_queue({
    'timestamp': str(time.mktime(time.gmtime())),
    'role': 'docker',
    'ip': '192.168.33.10',
    'password': 'foobar123',
    'username': 'root',
    'uuid': str(uuid4())
})

redis_helper.add_to_queue({
    'timestamp': str(time.mktime(time.gmtime())),
    'role': 'docker',
    'ip': '192.168.33.11',
    'password': 'foobar12',
    'username': 'root',
    'uuid': str(uuid4())
})
