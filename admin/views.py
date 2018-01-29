from admin import app, args
from flask import render_template, url_for, request, Blueprint, flash, redirect
from admin.utils import traversal, make_path
import sys, os
from admin.article import article_factory
from admin.forms import ArticleForm
import copy

admin_bp = Blueprint('admin', __name__)
article_bp = Blueprint('article', __name__, url_prefix='/article')

@admin_bp.route('/')
def index():
    path = args.path
    articles = []
    for full_path in traversal(path):
        article = article_factory(full_path)
        if article.meta.get('title', None):
            articles.append(article)

    print(articles)
    return render_template('index.html', articles = articles)


@article_bp.route('/edit', methods=['GET', 'POST'])
def edit():
    form = ArticleForm()
    path = request.args.get('path')
    article = article_factory(path)
    if request.method == 'GET':

        print(path)
        print(article)
        return render_template('article/edit.html', form=form, article=article)
        return path
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
