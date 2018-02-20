import sys, os
import re
from redbaron import RedBaron
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file, get_settings_from_module
from unipath import Path
import tempfile
import importlib
import pprint
import json

here = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    pass

class PelicanConfig(object):
    pass

class DefaultConfig(object):
    pass

# def get_settings_from_file(path, default_settings={}):
#     """Loads settings from a file path, returning a dict."""
#
#     name, ext = os.path.splitext(os.path.basename(path))
#     module = load_source(name, path)
#     return get_settings_from_module(module, default_settings=default_settings)

'''
DEFAULT_PELICAN_SETTINGS = {
    'SERVER_DEBUG': True
}
'''


def load_source(name, path):
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod

# def get_settings_from_file(path, default_settings = None):
#     if default_settings is None:
#         default_settings = {}
#     name, ext = os.path.splitext(os.path.basename(path))
#     module = load_source(name, path)
#     return get_settings_from_module(module, default_settings = default_settings)

class Config(object):
    ''' 代理类'''
    config_file = None

    def __init__(self, path = None):
        if path is None:
            path = os.path.join(os.getcwd(), 'pelicanconf.py')
        if self.config_file:
            path = self.config_file
        self._path = path
        self._pelicanconf = get_settings_from_file(self._path)
        self._baron = None

    def set(self, key, value):
        self.__dict__[key] = value

    def get(self, key, default = None):
        '''从 pelicanconf.py 中取出配置
        Args:
            key: 要取出的变量名
            default: 配置不存在时的默认值
        '''
        key = key.upper()
        return self._pelicanconf.get(key, default)


    def __getattr__(self, key):
        return self.get(key)

    def __setattr__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)


    def update(self, key, value):
        '''更新配置
        '''
        return self.set(key, value)

    def delete(self, key):
        ''' 删除 key 配置变量'''
        index = self.find_baron(key.upper())
        if index:
            del self.baron[index]
            print(self.baron)
            self.save()

    def find_baron(self, key):
        ''' 从 redbaron 中提取配置'''
        not_found = True
        index = None
        red = self.baron
        for i in range(0, len(red)):
            try:
                target = red[i].target.value
            except:
                target = ''
            if target == key:
                not_found = False
                index = i

        return index

    @property
    def baron(self):
        if not self._baron:
            with open(self._path, 'r') as fp:
                text = fp.read()
            red = RedBaron(text)
            self._baron = red

        return self._baron

    def save(self):
        ''' 保存配置到 self._path '''
        keys = [k for k in self.__dict__.keys() if k[0] != '_']
        red = self.baron
        for key in keys:
            up_key = key.upper()
            not_found = True
            for i in range(0, len(red)):
                try:
                    target = red[i].target.value
                except:
                    target = ''
                if target == up_key:
                    not_found = False
                    value = self.__dict__[key]
                    if isinstance(value, str):
                        value = '"{}"'.format(value)
                    elif isinstance(value, dict):
                        # value = "{}".format(value)
                        print("DICT")
                        # multi = json.loads(value)
                        value = json.dumps(value, indent=4)
                        print(value)
                        # value = dumps(value)
                    else:
                        value = "{}".format(value)
                    red[i].value = value

            if not_found:
                # 不存在， 在末尾新增
                format_ = '{key} = "{value}"'.format(key = key.upper(), value = self.__dict__[key])
                red.append(format_)


        with open(self._path, 'w') as fp:
            text = red.dumps()
            fp.write(text)

        # 清除缓存
        self._baron = None


    @classmethod
    def monkey_patch(cls, path):
        cls.config_file = path
