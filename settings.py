# Django-style settings file
import os


def str2bool(s):
    return s.lower() in ['true', '1', 'yes']

REDIS_SERVER = os.getenv('REDIS_PORT_6379_TCP_ADDR', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT_6379_TCP_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 0)
REDIS_LIST = 'prov'

SINGLE_HOST_PLAYBOOKS = [
    'docker',
    'docker_registry',
    'drupal',
    'elasticsearch',
    'fluentd',
    'gitlab',
    'grafana',
    'jenkins',
    'joomla',
    'kibana',
    'letsencrypt',
    'mongodb',
    'mysql',
    'nginx',
    'owncloud',
    'postgres',
    'prometheus',
    'prometheus_node_exporter'
    'redis',
    'redmine',
    'wordpress',
]

CLUSTER_PLAYBOOKS = [
    'nodebb',
    'mongodb',
    'weave',
]

META_PACKAGES = [
    'meta_logging_appliance',
]

PLAYBOOKS = SINGLE_HOST_PLAYBOOKS + CLUSTER_PLAYBOOKS + META_PACKAGES

# Provide a comma separated list
HIDDEN_PLAYBOOKS = os.getenv(
    'HIDDEN_PLAYBOOKS',
    'nginx,prometheus_node_exporter'
).split(',')

MODULES = [
    'ping',
    'ssh-keys',
]


REMOTE_USER = os.getenv('REMOTE_USER', 'root')
SSH_PRIVATE_KEYS = os.getenv('SSH_PRIVATE_KEYS', '')

# Redirect all webapps to HTTPS instead of HTTP
USE_SSL = str2bool(os.getenv('USE_SSL', 'True'))
