# Django-style settings file
import os

REDIS_SERVER = os.getenv('REDIS_PORT_6379_TCP_ADDR', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT_6379_TCP_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 0)
REDIS_LIST = 'prov'

SINGLE_HOST_PLAYBOOKS = [
    'dns',
    'docker',
    'docker_registry',
    'drupal',
    'joomla',
    'letsencrypt',
    'mongodb',
    'mysql',
    'owncloud',
    'postgres',
    'redis',
    'redmine',
    'wordpress',
]

CLUSTER_PLAYBOOKS = [
    'nodebb',
    'mongodb',
    'weave',
]

PLAYBOOKS = SINGLE_HOST_PLAYBOOKS + CLUSTER_PLAYBOOKS

HIDDEN_PLAYBOOKS = [
    'dns',
    'letsencrypt',
]

MODULES = [
    'ping',
    'ssh-keys',
]
