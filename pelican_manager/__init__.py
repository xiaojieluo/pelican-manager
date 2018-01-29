from flask import Flask
from pelican_manager.config import Args

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Security'
app.debug = True

# 命令行参数实例类
args = Args()

from pelican_manager.views import admin_bp, article_bp
app.register_blueprint(admin_bp)
app.register_blueprint(article_bp)
