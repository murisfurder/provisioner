import redis
import settings
import socket
import redis_lock


def connect():
    r = redis.StrictRedis(
        host=settings.REDIS_SERVER,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB
    )
    return r


def pubsub():
    r = connect()
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe(settings.REDIS_CHANNEL)
    return p


def get_lock(uuid):
    return redis_lock.Lock(
        connect(),
        uuid,
        id=socket.gethostname(),
        expire=3600,
    )


def get_status(uuid):
    r = connect()
    return r.get(uuid)


def push_status(ip=None, status=None, ttl=3600):
    r = connect()
    return r.setex(ip, ttl, status)
