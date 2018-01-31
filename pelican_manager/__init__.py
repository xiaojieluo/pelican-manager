from flask import Flask
from pelican_manager.config import Config

def make_app():
    config = Config()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Security'
    # app.debug = config['server']['debug']
    app.debug = False

    from pelican_manager.views import admin_bp, article_bp
    app.register_blueprint(admin_bp)
    app.register_blueprint(article_bp)

    return app
