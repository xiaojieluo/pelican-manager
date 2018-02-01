from flask import current_app, render_template, url_for, request, Blueprint, flash, redirect
from pelican_manager.utils import traversal
import sys, os
from pelican_manager.article import article_factory
from pelican_manager.forms import ArticleForm, SettingForm
import copy
from .config import Config
import toml

admin_bp = Blueprint('admin', __name__)
article_bp = Blueprint('article', __name__, url_prefix='/article')

@admin_bp.route('/')
def index():
    config = Config()
    path = os.path.join(os.getcwd(), config['blog']['path'])
    articles = []
    for full_path in traversal(path):
        article = article_factory(full_path)
        if article and article.meta.get('title', None):
            articles.append(article)

    return render_template('index.html', articles = articles)

@admin_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingForm()
    config = Config()
    if request.method == 'POST':
        if form.validate_on_submit():
            config.update(form.data)
            config.save()
            path = os.path.join(os.getcwd(), 'pelican_manager.toml')
            flash("保存配置到 {}.".format(path))
            return redirect(url_for('admin.settings'))
        else:
            flash("表单验证失败！")
    else:
        return render_template('settings.html', form=form, config = config)

@article_bp.route('/edit', methods=['GET', 'POST'])
def edit():
    form = ArticleForm()
    path = request.args.get('path')
    article = article_factory(path)
    if request.method == 'GET':
        return render_template('article/edit.html', form=form, article=article)
    else:
        if form.validate_on_submit():
            data = copy.deepcopy(form.data)
            if 'csrf_token' in data:
                data.pop('csrf_token')
            for k, v in data.items():
                article.update_meta(k, v)
            article.save()
            flash("保存成功！")
            return redirect(url_for('admin.index'))
