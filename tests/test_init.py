from flask import Flask
from pelican_manager import make_app

def test_make_app():
    path = 'tests/pelicanconf.py'
    app = make_app(path)
    
    assert isinstance(app, Flask)
