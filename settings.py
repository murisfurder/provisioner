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
    'grafana',
    'joomla',
    'letsencrypt',
    'mongodb',
    'mysql',
    'nginx',
    'owncloud',
    'postgres',
    'prometheus',
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
    'letsencrypt,'
    'nginx',
]

MODULES = [
    'ping',
    'ssh-keys',
]


REMOTE_USER = os.getenv('REMOTE_USER', 'root')
SSH_PRIVATE_KEYS = os.getenv('SSH_PRIVATE_KEYS', '')
