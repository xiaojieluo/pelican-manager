import pytest
from pelican_manager.config import Config
from pelican_manager import make_app
import json
from pelican_manager.utils import iterdir

@pytest.fixture()
def client(request):
    app = make_app('tests/pelicanconf.py')
    app.config['TESTING'] = True
    client = app.test_client()

    def teardown():
        app.config['TESTING'] = False
    request.addfinalizer(teardown)
    return client

def test_get_all_articles_lists_GET(client):
    url = '/api/articles/'
    res = client.get(url)

    assert res.status_code == 200
    data = res.data.decode('utf-8')
    data = json.loads(data)
    assert isinstance(data, dict)
    assert 'results' in data
    assert 'total' in data
    assert isinstance(data['total'], int)
    assert isinstance(data['results'], list)


PATHS = [path for path in iterdir('tests/content')]

@pytest.fixture(params = PATHS)
def path(request):
    return request.param

def test_get_one_article_info_GET(client, path):
    url = '/api/articles/{}'.format(path)
    res = client.get(url)
    assert res.status_code == 200
