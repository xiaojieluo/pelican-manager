import pytest
from admin.config import Config
import sys, os

@pytest.fixture()
def path(request):
    return 'tests/pelicanconf.py'

def test_get_pelican_config(path):
    config = Config(path)
    assert config.AUTHOR == 'Xiaojie Luo'
