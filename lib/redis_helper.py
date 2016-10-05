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


def get_jobs():
    jobs = []
    r = connect()
    for job in r.scan_iter():
        jobs.append(job)
    return jobs


def create_status(uuid, role, ip):

    if not uuid and role and ip:
        return False

    r = connect()
    timestamp = str(time.mktime(time.gmtime()))
    payload = {
        'role': role,
        'status': 'New',
        'ip': ip,
        'created_at': timestamp,
        'last_update_at': timestamp,
        'attempts': 0,
        'msg': [],
        'install_notes': ''
    }
    return r.set(uuid, json.dumps(payload))


def update_status(
    uuid=None,
    status=None,
    attempts=None,
    msg=None,
    install_notes=None,
):

    if not uuid:
        return False

    r = connect()
    job_status = get_status(uuid)

    job_status['last_update_at'] = str(time.mktime(time.gmtime()))
    job_status['attempts'] = attempts if attempts else job_status['attempts']
    job_status['status'] = status if status else job_status['status']
    job_status['install_notes'] = install_notes if install_notes else job_status['install_notes']

    if msg:
        job_status['msg'].append(msg)

    return r.set(uuid, json.dumps(job_status))


def get_redis_status():
    r = connect()
    return json.dumps(r.info())
