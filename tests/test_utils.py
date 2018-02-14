import pytest
from pelican_manager.utils import iterdir
import os, sys
import types

def test_iterdir():
    path = 'tests/content'
    files = iterdir(path)
    assert isinstance(files, types.GeneratorType)
