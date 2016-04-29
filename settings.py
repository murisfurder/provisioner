# Django-style settings file
import os

REDIS_SERVER = os.getenv('REDIS_PORT_6379_TCP_ADDR', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT_6379_TCP_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 0)
REDIS_LIST = 'prov'

STATUS_LIFETIME = 24 * 3600

SINGLE_HOST_PLAYBOOKS = [
    'docker',
    'docker_registry',
    'mongodb',
    'mysql',
    'postgres',
    'redis',
    'wordpress',
]

CLUSTER_PLAYBOOKS = [
    'nodebb',
    'mongodb',
    'weave',
]

PLAYBOOKS = SINGLE_HOST_PLAYBOOKS + CLUSTER_PLAYBOOKS

MODULES = [
    'ping',
    'ssh-keys',
]
