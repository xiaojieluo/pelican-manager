import pytest
from pelican_manager.config import Config
import sys, os




def back(path):
    text = None
    with open('tests/config/pelicanconf.py', 'r') as fp:
        text = fp.read()
    with open(path, 'w') as fp:
        fp.write(text)

@pytest.fixture()
def config(request):
    path = 'tests/pelicanconf.py'
    back(path)

    with open(path, 'r') as fp:
        content = fp.read()

    def teardown():
        back(path)

    request.addfinalizer(teardown)
    return Config(path)

def test_get_config(config):
    assert config.path == 'content'
    assert config.PATH == 'content'
    assert config['path'] == 'content'
    assert config['PATH'] == 'content'

def test_config_without_path():
    config = Config('tests/config/pelican_none.py')
    path = 'tests/config/pelican_none.py'
    assert config._path == path

def test_config_default_server_setting(config):
    assert config.server_port == 5000
    assert config.server_debug is True

def test_config_get_with_default(config):
    assert config.get('server_none', None) is None

def test_config_update(config):
    name = 'server_none2'
    key = None
    config.update(name, key)
    assert config.__dict__[name] == key

def test_config_save(config):
    test_data = [
        ('test_bool', None),
        ('test_int', 10),
    ]

    for data in test_data:
        key, value = data
        attr_str = "{} = {}".format(key.upper(), value)
        config.update(key, value)
        config.save()
        with open(config._path) as fp:
            lines = fp.read().split('\n')

        assert attr_str in lines
        # lines.remove(attr_str)
        # with open(config._path, 'w') as fp:
        #     text = '\n'.join(lines)
        #     fp.write(text)


def test_config():
    config = Config('tests/pelicanconf.py')
    print(config._path)

#
#
# def test_config(config):
#     print(config._path)
#     print(config.server_port)

# def test_config_default(config):
# def test_config():
#     config = Config()
#     print(dir(config))
#     print(config.__dict__)
#     print(config.server_port)
#     # config.server_port = 5000
#     # print(config.server_port)
#     # print(config.__dict__)
#
# def test_config_save():
#     config = Config()
#     config.path = 'test/content'
#     config.server_port = 5000
#     config.save()
#
# # ========
# @pytest.fixture()
# def path(request):
#     # return request.param
#     return 'tests/pelicanconf.py'
#
# def test_get_pelican_config(path):
#     config = PelicanConfig(path)
#     assert config.AUTHOR == 'Xiaojie Luo'
#     assert config.Nothing == None
#
#     assert config['AUTHOR'] == 'Xiaojie Luo'
#     assert config['Nothing'] == None
#
# @pytest.fixture()
# def config(request):
#     config = Config()
#     return config
#
# def test_pelican_manager_default_config(config):
#     # config = Config()
#     assert config['server']['debug'] == True
#     assert config['server']['port'] == 5000
#
#
# def test_config_update(config):
#     data = {'debug': False, 'port' : 5002}
#     config.update(data)
#
#     config.update(path = 'content')
#
#     assert config['server']['debug'] == False
#     assert config['server']['port'] == 5002
#     assert config['blog']['path'] == 'content'
#
# # def test_config_singlation():
# #     config1 = Config()
# #     config2 = Config()
# #     assert id(config1) == id(config2)
#
# def test_filter_data(config):
#     data = {'debug': False, 'port': 5002}
#     new_data = config.filter_data(data)
#     assert new_data == {'server': {'debug':False, 'port': 5002}}
#
# def test_config_save( config):
#     config.save()
#     path = os.path.join(os.getcwd(), 'pelican_manager.toml')
#     assert os.path.exists(path) is True
