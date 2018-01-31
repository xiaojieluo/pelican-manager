import pytest
from pelican_manager.config import PelicanConfig, Config
import sys, os

@pytest.fixture()
def path(request):
    # return request.param
    return 'tests/pelicanconf.py'

def test_get_pelican_config(path):
    config = PelicanConfig(path)
    assert config.AUTHOR == 'Xiaojie Luo'
    assert config.Nothing == None

    assert config['AUTHOR'] == 'Xiaojie Luo'
    assert config['Nothing'] == None

@pytest.fixture()
def config(request):
    config = Config()
    return config

def test_pelican_manager_default_config(config):
    # config = Config()
    assert config['server']['debug'] == True
    assert config['server']['port'] == 5000


def test_config_update(config):
    data = {'debug': False, 'port' : 5002}
    config.update(data)

    config.update(path = 'content')

    assert config['server']['debug'] == False
    assert config['server']['port'] == 5002
    assert config['blog']['path'] == 'content'

# def test_config_singlation():
#     config1 = Config()
#     config2 = Config()
#     assert id(config1) == id(config2)

def test_filter_data(config):
    data = {'debug': False, 'port': 5002}
    new_data = config.filter_data(data)
    assert new_data == {'server': {'debug':False, 'port': 5002}}

def test_config_save( config):
    config.save()
    path = os.path.join(os.getcwd(), 'pelican_manager.toml')
    assert os.path.exists(path) is True
