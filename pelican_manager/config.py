import sys, os
import re
from redbaron import RedBaron
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file, get_settings_from_module
from unipath import Path
import tempfile
import importlib

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

    def save(self):
        ''' 保存配置到 self._path '''
        keys = [k for k in self.__dict__.keys() if k[0] != '_']
        with open(self._path, 'r') as fp:
            text = fp.read()

        red = RedBaron(text)
        for key in keys:
            key = key.upper()
            for i in range(0, len(red)):
                try:
                    target = red[i].target.value
                except:
                    target = ''
                if target == key:
                    value = self.__dict__[key.lower()]
                    if isinstance(value, str):
                        value = "'{}'".format(value)
                    else:
                        value = "{}".format(value)
                    red[i].value = value

        with open(self._path, 'w') as fp:
            text = red.dumps()
            fp.write(text)


    @classmethod
    def monkey_patch(cls, path):
        cls.config_file = path




# class Config_bak(object):
#     # monkey patch
#     # 保存从命令行传入的 config file path
#     config_file = None
#
#     def __init__(self, path = None):
#         if path is None:
#             path = os.path.join(os.getcwd(), 'pelicanconf.py')
#         if self.config_file:
#             path = self.config_file
#
#         self._path = path
#         self._pelicanconf = self.make_config(path, 'pelicanconf')
#         here = os.path.abspath(os.path.dirname(__file__))
#         default_path = os.path.join(here, 'config/defaultconf.py')
#         self._default = self.make_config(default_path, 'defaultconf')
#
#
#     @classmethod
#     def monkey_patch(cls, path):
#         cls.config_file = path
#
#     @property
#     def base_path(self):
#         print(self._path)
#
#
#     def set(self, key, value):
#         self.__dict__[key] = value
#
#     def get(self, key, default = None):
#         '''从 pelicanconf.py 中取出配置
#         Args:
#             key: 要取出的变量名
#             default: 配置不存在时的默认值
#         '''
#         key = key.upper()
#         if key in self._pelicanconf.__dir__():
#             return getattr(self._pelicanconf, key)
#         elif key in self._default.__dir__():
#             return getattr(self._default, key)
#         return default
#
#     @property
#     def date_format(self):
#         ''' 日期格式'''
#         locale = self.get('default_lang', 'en')
#         date_format = self.get('date_format')
#         if date_format and locale in date_format:
#             return date_format[locale]
#         else:
#             return self.get('default_date_format')
#
#     def update(self, key, value):
#         '''更新配置
#         '''
#         return self.set(key, value)
#
#     def save(self):
#         ''' 保存环境变量到 self._path 路径'''
#         update = []
#         lines = []
#         # if os.path.exists(self._path):
#         with open(self._path, 'r') as fp:
#             lines = fp.read().split('\n')
#
#         for key, value in list(self.__dict__.items()):
#             # 排除掉开头为下划线的内部变量
#             if key[0] != '_':
#                 key = key.upper()
#                 if key == 'page_hide_column':
#                     value = ','.split(value)
#                 def filter_func(line):
#                     match = re.match(r'^{}(\s.*)=(.*)'.format(key), line)
#                     if match:
#                         return True
#                 result = list(filter(filter_func, lines))
#                 if isinstance(value, str):
#                     value = '\'{}\''.format(value)
#                 attribute = '{key} = {value}'.format(key=key, value=value)
#                 if result:
#                     index = lines.index(result[0])
#                     lines[index] = attribute
#                 else:
#                     if key == 'SERVER_PORT':
#                         lines.append('# Server running port.')
#                     lines.append(attribute)
#                 # 删除更新过的 key
#                 try:
#                     del self.__dict__[key.lower()]
#                 except KeyError as e:
#                     del self.__dict__[key.upper()]
#                 else:
#                     print("未知 key:{}".format(key))
#
#         text = '{}'.format(os.linesep).join(lines)
#         with open(self._path, 'w+') as fp:
#             fp.write(text)
#
#     def make_config(self, path, name):
#         '''make config'''
#         pelicanconf = import_module(name, path)
#         return pelicanconf
#
#     def __getattr__(self, key):
#         return self.get(key)
#
#     def __setattr__(self, key, value):
#         self.set(key, value)
#
#     def __getitem__(self, key):
#         return self.get(key)
