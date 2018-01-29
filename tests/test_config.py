import pytest
from pelican_manager.config import Config
import sys, os

@pytest.fixture()
def path(request):
    return 'tests/pelicanconf.py'

def test_get_pelican_config(path):
    config = Config(path)
    assert config.AUTHOR == 'Xiaojie Luo'
