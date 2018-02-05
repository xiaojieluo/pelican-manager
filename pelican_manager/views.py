from flask import (current_app, render_template, url_for, request, Blueprint,
                    flash, redirect,abort)
from pelican_manager.utils import traversal
import sys, os
from pelican_manager.article import article_factory
from pelican_manager.forms import ArticleForm, SettingForm
import copy
from .config import Config

admin_bp = Blueprint('admin', __name__)
article_bp = Blueprint('article', __name__, url_prefix='/article')

@admin_bp.route('/')
def index():
    config = Config()
    paths = [os.path.join(os.getcwd(), config.path)]
    if config.article_paths:
        for path in config.article_paths:
            paths = list(map(lambda p: os.path.join(p, path), paths))
    articles = []
    for path in paths:
        for full_path in traversal(path):
            article = article_factory(full_path)
            if article and article.meta.get('title', None):
                articles.append(article)
    # return pjax('index.html', articles=articles)
    return render_template('index.html', articles = articles)

@admin_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingForm()
    config = Config()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = copy.copy(form.data)
            data['server_debug'] = bool(data['server_debug'])
            for k, v in data.items():
                if k != 'csrf_token':
                    config.update(k, v)
            config.save()
            flash("保存配置到 {}.".format(config._path))
        else:
            flash("表单验证失败！")
        return redirect(url_for('admin.settings'))
    else:
        return render_template('settings.html', form=form, config = config)

@article_bp.route('/edit', methods=['GET', 'POST'])
def edit():
    form = ArticleForm()
    path = request.args.get('path')
    if path is None:
        abort(405)
    article = article_factory(path)
    if request.method == 'POST':
        if form.validate_on_submit():
            data = copy.deepcopy(form.data)
            if 'csrf_token' in data:
                data.pop('csrf_token')
            for k, v in data.items():
                article.update_meta(k, v)
            article.save()
            flash("保存成功！")
        else:
            flash("保存失败。")
        return redirect(url_for('admin.index'))
    else:
        return render_template('article/edit.html', form=form, article=article)

# def pjax(template, pjax_block='content', **kwargs):
#     if "X-PJAX" in request.headers:
#         app = current_app
#         app.update_template_context(kwargs)
#         template = app.jinja_env.get_template(template)
#         block = template.blocks[pjax_block]
#         context = template.new_context(kwargs)
#         return ''.join(block(context))
#     else:
#         return render_template(template, **kwargs)
