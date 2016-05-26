import os
from bottle import template


def get_docs(role, extra_vars):
    docs_uri = 'provision_profiles/{}_install_notes.tpl'.format(role)

    if not os.path.isfile(docs_uri):
        return 'No installation notes available.'

    try:
        install_notes = template(docs_uri, **extra_vars)
        return install_notes
    except:
        return 'Failed to process installation notes.'
