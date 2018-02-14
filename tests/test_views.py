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

def test_index(client):
    assert client.get('/').status_code == 200
