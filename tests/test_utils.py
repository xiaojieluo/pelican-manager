import pytest
from pelican_manager.utils import traversal, import_module, NotFoundPelicanConfig, Translate
import os, sys


def test_import_module():
    name = 'pelicanconf'
    path = os.path.join(os.getcwd(), __file__)

    pelicanconf = import_module(name, path)
    assert pelicanconf is not None

def test_import_module_exception():
    name = 'pelicanerror'
    path = './'
    with pytest.raises(NotFoundPelicanConfig):
        pelicanconf = import_module(name, path)

def test_traversal():
    path = 'tests/content'
    files = traversal(path)
    assert 'tests/content/test.md' in files

def test_translate():
    appid = '2012512b6990f8ae'
    appkey = 'GqYuFjdV404u21UAMLCFgF3iVMGchf1g'
    trans = Translate('youdao', appid, appkey)
    print(trans.translate('去你妈的， 你他妈是谁啊'))
