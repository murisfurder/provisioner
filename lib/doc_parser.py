import logging
import os
from bottle import template


def get_docs(role=None, extra_vars=None):
    script_path = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_path, '..'))

    docs_uri = '{}/provision_profiles/{}_install_notes.tpl'.format(
        project_root,
        role
    )

    if not os.path.isfile(docs_uri):
        return 'No installation notes available.'

    try:
        install_notes = template(docs_uri, **extra_vars)
        return install_notes
    except Exception as e:
        logging.exception("Failed to process install notes")
        return 'Failed to process installation notes.'
