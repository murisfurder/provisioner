from nose.tools import eq_, assert_in
from lib import doc_parser


def test_non_existing_docs():
    r = doc_parser.get_docs(role='foobar')
    eq_(r, 'No installation notes available.')


def test_drupal_without_vars():
    r = doc_parser.get_docs(role='drupal')
    eq_(r, 'Failed to process installation notes.')


def test_drupal_with_vars():
    r = doc_parser.get_docs(
        role = 'drupal',
        extra_vars={
            'role': 'drupal',
            'public_ip': '127.0.0.1',
            'mysql_drupal_user': 'foobar',
            'mysql_drupal_password': 'foobar',
        }
    )
    assert_in('Congratulations!', r)
