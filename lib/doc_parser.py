import os
from bottle import template


def get_docs(role, extra_vars):
    docs_uri = 'provision_profiles/{}.tpl'.format(role)

    if not os.path.isfile(docs_uri):
        return 'No installation notes available.'

    try:
        install_docs = template(docs_uri, **extra_vars)
        return install_docs
    except:
        return 'Failed to process installation notes.'
