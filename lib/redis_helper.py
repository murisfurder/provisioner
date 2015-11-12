import redis
import settings


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
