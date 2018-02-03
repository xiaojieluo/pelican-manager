import pytest
from flask import Flask, url_for
from pelican_manager import make_app
from pelican_manager.config import Config

@pytest.fixture()
def client(request):
    app = make_app('tests/pelicanconf.py')
    app.config['TESTING'] = True
    client = app.test_client()

    def teardown():
        app.config['TESTING'] = False
    request.addfinalizer(teardown)
    return client

def test_admin_index(client):
    assert client.get('/').status_code == 200
    assert client.post('/').status_code == 405

def test_admin_setting(client):
    assert client.get('/settings').status_code == 200
    assert client.post('/settings').status_code == 302

def test_article_edit(client):
    # url = url_for('article/edit', path='tests/content/test.md')
    url = 'article/edit?path=tests/content/test.md'
    assert client.get(url).status_code == 200
    assert client.post(url).status_code == 302
