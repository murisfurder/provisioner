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
    'gitlab',
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

# Provide a comma separated list
HIDDEN_PLAYBOOKS = os.getenv(
    'HIDDEN_PLAYBOOKS',
    'dns,nginx'
).split(',')

MODULES = [
    'ping',
    'ssh-keys',
]


REMOTE_USER = os.getenv('REMOTE_USER', 'root')
SSH_PRIVATE_KEYS = os.getenv('SSH_PRIVATE_KEYS', '')

# Redirect all webapps to HTTPS instead of HTTP
USE_SSL = bool(os.getenv('USE_SSL', True))
