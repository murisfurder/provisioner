import json
import redis
import settings
import time


def connect():
    r = redis.StrictRedis(
        host=settings.REDIS_SERVER,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB
    )
    return r


def add_to_queue(msg):
    r = connect()
    push_status(
        uuid=msg['uuid'],
        ip=msg['ip'],
        status='Queued',
        attempts=msg['attempts']
    )
    return r.rpush(settings.REDIS_LIST, json.dumps(msg))


def pop_from_queue():
    """
    Pull the oldest message from the queue.
    """
    r = connect()
    msg = r.lpop(settings.REDIS_LIST)
    if msg:
        try:
            return json.loads(msg)
        except:
            print 'Unable to load message:\n{}'.format(msg)
            return False
    else:
        return False


def get_status(uuid):
    r = connect()
    payload = r.get(uuid)
    try:
        return json.loads(payload)
    except:
        print 'Unable to load message:\n{}'.format(payload)
        return False


def push_status(
    role=None,
    uuid=None,
    ip=None,
    status=None,
    attempts=None,
    ttl=3600
):
    r = connect()
    timestamp = str(time.mktime(time.gmtime()))
    payload = {
        'role': role,
        'status': status,
        'ip': ip,
        'timestamp': timestamp,
        'attempts': attempts,
    }
    return r.setex(uuid, ttl, json.dumps(payload))
