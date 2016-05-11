
NODE_USERNAME = 'vagrant'
NODE_PASSWORD = 'foobar123'
NODES = [
    {'name': 'vm0', 'ip': '192.168.33.10', 'username': NODE_USERNAME, 'password': NODE_PASSWORD},
    {'name': 'vm1', 'ip': '192.168.33.11', 'username': NODE_USERNAME, 'password': NODE_PASSWORD},
    {'name': 'vm2', 'ip': '192.168.33.12', 'username': NODE_USERNAME, 'password': NODE_PASSWORD},
]

EXIT_STATUS = ['Aborted', 'Done', 'Error', 'Failed']

from site_settings import *
