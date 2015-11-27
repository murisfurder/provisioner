import json
import redis
import settings


def connect():
    r = redis.StrictRedis(
        host=settings.REDIS_SERVER,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB
    )
    return r


def add_to_queue(msg):
    r = connect()
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
    return r.get(uuid)


def push_status(ip=None, status=None, ttl=3600):
    r = connect()
    return r.setex(ip, ttl, status)
