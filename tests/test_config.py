import pytest
from pelican_manager.config import Config
import sys

@pytest.fixture()
def config(request):
    config  = Config('tests/pelicanconf.py')
    return config

def test_config_get(config):
    assert config.SITEURL == 'Test'
    assert isinstance(config.STATIC_PATHS, list)

def test_config_set(config):
    config.default_lang = 'zh'
    config.save()

    # back
    assert config.default_lang == 'zh'
    config.default_lang = 'en'
    config.save()
