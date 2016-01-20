import json
import redis
import settings
import time

TTL = 24 * 3600

def connect():
    r = redis.StrictRedis(
        host=settings.REDIS_SERVER,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB
    )
    return r


def add_to_queue(task):
    r = connect()
    push_status(
        uuid=task['uuid'],
        ip=task['ip'],
        status='Queued',
        attempts=task['attempts']
    )
    return r.rpush(settings.REDIS_LIST, json.dumps(task))


def pop_from_queue():
    """
    Pull the oldest message from the queue.
    """
    r = connect()
    task = r.lpop(settings.REDIS_LIST)
    if task:
        try:
            return json.loads(task)
        except:
            print 'Unable to load message:\n{}'.format(task)
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
    return r.setex(uuid, TTL, json.dumps(payload))


def abort_job(uuid):
    r = connect()
    status = get_status(uuid)
    status['status'] = 'Aborted'
    status['timestamp'] = str(time.mktime(time.gmtime()))
    return r.setex(uuid, TTL, json.dumps(status))


def get_redis_status():
    r = connect()
    return json.dumps(r.info())
