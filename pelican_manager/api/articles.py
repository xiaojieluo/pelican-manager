from flask import current_app, Blueprint, request, abort
# from flask_restful import Resource, Api
from pelican_manager.config import Config
from pelican_manager.article import article_factory
from pelican_manager.utils import iterdir
import os
from flask_restplus import Resource, Api, reqparse, marshal_with, cors
import datetime
from slugify import slugify
import time
from .fields import article_list_fields, article_fields
import types
from schema import Schema
import urllib.parse
from pathlib import Path

app = current_app
article_api = Blueprint('article_api', __name__, url_prefix='/api/articles')
api = Api(article_api)

def parse_article_args():
    config = Config()
    parser = reqparse.RequestParser()
    parser.add_argument('path', type=str, location='json', default=None, help='文章保存地址')
    parser.add_argument('meta', type=dict, location='json', default=None, help='文章元数据')
    parser.add_argument('text', type=str, location='json', default='', help='文章不含元数据的正文')
    parser.add_argument('type', type=str, location='json', default='markdown', help='文章类型(markdown, rst)')
    args = parser.parse_args()
    if args['meta'] is None:
        args['meta'] = {}
    meta = args['meta']
    if meta.get('slug', None) is None:
        title = meta.get('title', '')
        meta['slug'] = slugify(title)
    meta['date'] = meta.get('date', datetime.datetime.now().strftime(config.default_date_format))
    meta['modified'] = meta.get('modified', datetime.datetime.now().strftime(config.default_date_format))

    ext = 'md' if args['type'] == 'markdown' else 'rst'
    args['location'] = args.get('path', '{}.{}'.format(meta.get('title', ''), ext))
    args['path'] = args['location']
    args['meta'] = meta
    print(args)
    return args

def cache(func):
    '''
    TODO
    缓存'''
    def wrapper(*args, **kw):
        result = func(*args, **kw)
        return result
    return wrapper

def filter_api(func):
    '''
    api 参数控制：
    key: 返回的字段， 当前面带 - 时表示不返回此项， 多个用,分隔
    '''
    def wrapper(*args, **kw):
        keys = request.args.get('key', '')
        exclude = []
        only = []
        if keys:
            keys = keys.split(',')
            for key in keys:
                if key and key[0] == '-':
                    exclude.append(key[1:])
                else:
                    only.append(key)
        datas = func(*args, **kw)
        if isinstance(datas, types.GeneratorType):
            result = []
            for data in datas:
                if only:
                    data = {k:v for k, v in data.items() if k in only}
                data = {k:v for k, v in data.items() if k not in exclude}
                result.append(data)
            return {'results':result, 'total': len(result)}
        else:
            if only:
                datas = {k:v for k, v in datas.items() if k in only}
            datas = {k:v for k, v in datas.items() if k not in exclude}
            return datas
    return wrapper


class ArticleAPI(Resource):
    @filter_api
    def get(self, path):
        config = Config()
        # print(path)
        # full_path = os.path.join(config.path or '', path)

        # article = article_factory(full_path)
        article = article_factory(path)
        if article is None:
            return {'err_code': 101, 'msg': '此格式暂不支持'}
        if os.path.exists(article.full_path):
            data = {
                'meta': article.meta,
                'path': article.path,
                'text': article.text
            }
            return data
        else:
            return {'err_code': 100, 'msg': '此文章不存在', 'full_path': article.full_path}

    def put(self, path):
        ''' 更新指定的文章
        目录不存在就抛出异常
        '''
        args = request.json
        config = Config()
        text = args.get('text', '')
        path = urllib.parse.unquote(path)
        article = article_factory(path)
        if article.exists() is not True:
            return {'error_msg':'文章不存在'}

        meta = args.get('meta', {})
        # 更新修改时间
        if 'modified' not in meta:
            meta['modified'] = datetime.datetime.now().strftime(config.date_format)
        article.meta = meta
        article.text = args.get('text', '')
        print(article.meta)
        article.save()
        return {'msg': '更新成功！'}

    def patch(self, path):
        ''' 部分更新'''
        args = request.json
        config = Config()
        path = urllib.parse.unquote(path)
        # full_path = os.path.join(config.path or '', path)
        article = article_factory(path)

        meta = args.get('meta', {})
        for k, v in meta.items():
            article.update_meta(k, v)
        if args.get('text', None):
            article.text = text
        article.save()
        return {'msg': 'update success.'}


    def delete(self, path):
        config = Config()
        full_path = os.path.join(config.path or '', path)
        try:
            os.remove(full_path)
            dir_, _ = os.path.dirname(full_path)
            os.removedirs(dir_)
        except:
            pass
        return {'status':'success.'}



class ArticleListApi(Resource):

    def options(self):
        ''' 跨域'''
        print("OPTIONS.")
        pass
    '''
    文件扫描规则：
        记录下文件夹的 st_mtime , 并将值和文件列表序列化到文件中，
        当分页时， 如果st_mtime 已修改则重新扫描目录， 重复上述步骤。
    返回值为 生成器， 需要 filter_api 装饰器进一步处理后才可以得到想要的的数据
    '''
    @filter_api
    def get(self):
        config = Config()
        paths = [config.path]
        if config.article_paths:
            for path in config.article_paths:
                paths = list(map(lambda p: os.path.join(p, path), paths))
        articles = []
        for path in paths:
            for full_path in iterdir(path):
                article = article_factory(full_path)
                if article and article.meta.get('title', None):
                    data = {
                        'meta': article.meta,
                        'path': article.path,
                        'text': article.text,
                    }
                    # print(data)
                    yield data

    def post(self):
        ''' 创建一个新文章'''
        args = parse_article_args()
        article = article_factory(args['path'])
        article.meta = args['meta']
        article.text = args['text']
        article.save()
        app.logger.debug("写入文件 {} 成功！".format(article.path))

        return {'msg': '写入成功'}, 201, {'Location': args['location']}

api.add_resource(ArticleAPI, '/<path:path>')
api.add_resource(ArticleListApi, '/')
