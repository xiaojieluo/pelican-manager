from flask import (current_app, render_template, url_for, request, Blueprint,
                    flash, redirect,abort)
from pelican_manager.utils import iterdir
import sys, os
from pelican_manager.article import article_factory
from pelican_manager.forms import ArticleForm, SettingForm, ServerSettingForm
import copy
from .config import Config

admin_bp = Blueprint('admin', __name__)
article_bp = Blueprint('article', __name__, url_prefix='/article')
setting_bp = Blueprint('setting', __name__, url_prefix='/setting')
app = current_app

@admin_bp.route('/')
def index():
    config = Config()
    return render_template('dist/index.html')
    # return render_template('article/index.html', config = config)

@setting_bp.route('/', methods=['GET', 'POST'])
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



@admin_bp.route('/count', methods=['GET', 'POST'])
def count():
    return "统计"

@setting_bp.route('/server', methods=['GET', 'POST'])
def server():
    config = Config()
    form = ServerSettingForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = copy.deepcopy(form.data)
            data['server_debug'] = bool(data['server_debug'])
            data['title_color_with_status'] = bool(data['title_color_with_status'])
            del data['csrf_token']
            for k, v in data.items():
                config.update(k, v)
            config.save()
            flash("保存配置到 {}".format(config._path), 'success')
        else:
            app.logger.debug(form.errors)
            flash("表单验证失败！", 'error')
        return redirect(url_for('setting.server'))
    else:
        return render_template('admin/server_setting.html', form=form, config = config)


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
        # return redirect(url_for('admin.index'))
    else:
        return render_template('article/edit.html', form=form, article=article)

def pjax(template, pjax_block='content', **kwargs):
    if "X-PJAX" in request.headers:
        app = current_app
        app.update_template_context(kwargs)
        template = app.jinja_env.get_template(template)
        block = template.blocks[pjax_block]
        context = template.new_context(kwargs)
        return ''.join(block(context))
    else:
        return render_template(template, **kwargs)
