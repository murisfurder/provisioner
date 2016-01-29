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
    update_status(uuid=task['uuid'], status='Queued')
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


def create_status(uuid, role, ip):

    if not uuid and role and ip:
        return False

    r = connect()
    timestamp = str(time.mktime(time.gmtime()))
    payload = {
        'role': role,
        'status': 'New',
        'ip': ip,
        'timestamp': timestamp,
        'attempts': 0,
        'msg': []
    }
    return r.setex(uuid, TTL, json.dumps(payload))


def update_status(
    uuid=None,
    status=None,
    attempts=None,
    msg=None
):

    if not uuid:
        return False

    r = connect()
    job_status = get_status(uuid)

    job_status['timestamp'] = str(time.mktime(time.gmtime()))
    job_status['attempts'] = attempts if attempts else job_status['attempts']
    job_status['status'] = status if status else job_status['status']
    if msg:
        job_status['msg'].append(msg)

    return r.setex(uuid, TTL, json.dumps(job_status))


def get_redis_status():
    r = connect()
    return json.dumps(r.info())
