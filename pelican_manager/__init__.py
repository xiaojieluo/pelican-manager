from flask import Flask
from pelican_manager.config import Config

def make_app(conf_path = None):
    '''
    Args:
        从命令行指定 config 的文件位置
    '''
    if conf_path:
        Config.monkey_patch(conf_path)

    config = Config()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Security'
    app.debug = config.server_debug

    from pelican_manager.views import admin_bp, article_bp
    app.register_blueprint(admin_bp)
    app.register_blueprint(article_bp)

    return app
