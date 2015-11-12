import time
import json
import settings
from lib import redis_helper

r = redis_helper.connect()

test_task = {
        'timestamp': str(time.mktime(time.gmtime())),
        'role': 'cloudcompose',
        'target_ips': ['192.168.33.10'],
        'password': 'foobar123',
        'username': 'root'
}

print r.publish(settings.REDIS_CHANNEL, json.dumps(test_task))
