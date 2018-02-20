from flask import current_app, Blueprint, request
from flask_restplus import Resource, Api, reqparse
from pelican_manager.config import Config
import types

app = current_app
setting_api = Blueprint('setting_api', __name__, url_prefix='/api/settings')
api = Api(setting_api)

def log():
    ''' 记录操作日志
    GET, POST
    '''

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
        if datas is None:
            return
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


def parse_setting_args():
    ''' 解析传入到 POST 的 body 参数'''
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, location='json')
    parser.add_argument('value', default='', location='json')
    args = parser.parse_args()
    return args

class SettingListApi(Resource):
    @filter_api
    def get(self):
        config  = Config()
        data = {k.lower(): v for k, v in config._pelicanconf.items()}
        return data

    def post(self):
        args = request.json
        if not isinstance(args, dict):
            return {'errCode': 301, 'msg': 'body 值错误！'}
        config = Config()
        for key, value in args.items():
            config.set(key, value)
        config.save()

        return {'status': 'successful.'}

class SettingApi(Resource):
    def get(self, name):
        config = Config()
        value = config.get(name)
        return {'status': '200', 'value': value}

    def put(self, name):
        config = Config()
        args = request.json
        if 'value' in args:
            config.set(name, args['value'])
            config.save()
            return {'status': 'successful'}
        else:
            return {'status': 'error.'}

    def delete(self, name):
        config = Config()
        config.delete(name)
        return {'message': '删除 {} 成功！'.format(name)}


api.add_resource(SettingApi, '/<string:name>')
api.add_resource(SettingListApi, '/')
