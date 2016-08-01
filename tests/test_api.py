import api
import json
import settings
from webtest import TestApp
from nose.tools import eq_, assert_not_equal

app = TestApp(api.app)


def test_root_page():
    r = app.get('/')
    eq_(r.body, 'Nothing to see here. Carry on.\n')


def test_roles_listing_without_hidden():
    r = app.get('/roles')
    assert_not_equal(r.json, settings.SINGLE_HOST_PLAYBOOKS)


def test_abort_without_job_provided():
    r = api.abort_job()
    r_json = json.loads(r)
    eq_(r_json['message'], 'No job specified.')


def test_get_job_status_without_job_provided():
    r = api.get_job_status()
    r_json = json.loads(r)
    eq_(r_json['message'], 'No job specified.')


def test_create_job_without_payload():
    r = app.post('/job', expect_errors=True)
    eq_(r.json['message'], 'Invalid JSON payload.')


def test_create_job_without_username():
    payload = {
        'ip': '127.0.0.1',
        'role': 'docker',
        'password': 'foobar',
    }
    r = app.post_json(
        '/job',
        payload,
        expect_errors=True
    )
    eq_(r.status_code, 400)
    eq_(
        r.json['message'],
        'Missing one of the required arguments.'
    )


def test_create_job_without_role():
    payload = {
        'ip': '127.0.0.1',
        'password': 'foobar',
        'username': 'foobar',
    }
    r = app.post_json(
        '/job',
        payload,
        expect_errors=True
    )
    eq_(r.status_code, 400)
    eq_(
        r.json['message'],
        'Missing one of the required arguments.'
    )


def test_create_job_with_invalid_role():
    payload = {
        'ip': '127.0.0.1',
        'password': 'foobar',
        'username': 'foobar',
        'role': 'foobar'
    }
    r = app.post_json(
        '/job',
        payload,
        expect_errors=True
    )
    eq_(r.status_code, 400)
    eq_(
        r.json['message'],
        'Invalid role.'
    )


def test_create_job_with_weave_without_extra_vars():
    payload = {
        'ip': '127.0.0.1',
        'password': 'foobar',
        'username': 'foobar',
        'role': 'weave'
    }
    r = app.post_json(
        '/job',
        payload,
        expect_errors=True
    )
    eq_(r.status_code, 400)
    eq_(
        r.json['message'],
        'Must be either master or slave.'
    )


def test_create_job_with_weave_slave_and_master():
    payload = {
        'ip': '127.0.0.1',
        'password': 'foobar',
        'username': 'foobar',
        'role': 'weave',
        'extra_vars': {
            'is_slave': True,
            'is_master': True,
        }
    }

    r = app.post_json(
        '/job',
        payload,
        expect_errors=True
    )
    eq_(r.status_code, 400)
    eq_(
        r.json['message'],
        'Must be master or slave. Not both.'
    )


def test_create_job_with_nodebb_without_secret():
    payload = {
        'ip': '127.0.0.1',
        'password': 'foobar',
        'username': 'foobar',
        'role': 'nodebb',
        'extra_vars': {'foo': 'bar'}
    }

    r = app.post_json(
        '/job',
        payload,
        expect_errors=True
    )
    eq_(r.status_code, 400)
    eq_(
        r.json['message'],
        'A secret is always required when using role nodebb.'
    )
