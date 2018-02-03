import sys, os
from .utils import import_module
import re

class Config(object):
    # monkey patch
    # 保存从命令行传入的 config file path
    config_file = None

    def __init__(self, path = None):
        if path is None:
            path = os.path.join(os.getcwd(), 'pelicanconf.py')
        if self.config_file:
            path = self.config_file

        self._path = path
        self._pelicanconf = self.make_config(path, 'pelicanconf')
        here = os.path.abspath(os.path.dirname(__file__))
        default_path = os.path.join(here, 'config/defaultconf.py')
        self._default = self.make_config(default_path, 'defaultconf')

    @classmethod
    def monkey_patch(cls, path):
        cls.config_file = path

    def set(self, key, value):
        self.__dict__[key] = value

    def get(self, key, default = None):
        '''从 pelicanconf.py 中取出配置
        Args:
            key: 要取出的变量名
            default: 配置不存在时的默认值
        '''
        key = key.upper()
        if key in self._pelicanconf.__dir__():
            return getattr(self._pelicanconf, key)
        elif key in self._default.__dir__():
            return getattr(self._default, key)
        return default

    def update(self, key, value):
        '''更新配置
        '''
        return self.set(key, value)

    def save(self):
        ''' 保存环境变量到 self._path 路径'''
        update = []
        lines = []
        # if os.path.exists(self._path):
        with open(self._path, 'r') as fp:
            lines = fp.read().split('\n')

        for key, value in list(self.__dict__.items()):
            # 排除掉开头为下划线的内部变量
            if key[0] != '_':
                key = key.upper()
                def filter_func(line):
                    match = re.match(r'^{}(\s.*)=(.*)'.format(key), line)
                    if match:
                        return True
                result = list(filter(filter_func, lines))
                if isinstance(value, str):
                    value = '\'{}\''.format(value)
                attribute = '{key} = {value}'.format(key=key, value=value)
                if result:
                    index = lines.index(result[0])
                    lines[index] = attribute
                else:
                    if key == 'SERVER_PORT':
                        lines.append('# Server running port.')
                    lines.append(attribute)
                # 删除更新过的 key
                try:
                    del self.__dict__[key.lower()]
                except KeyError as e:
                    del self.__dict__[key.upper()]
                else:
                    print("未知 key:{}".format(key))

        text = '{}'.format(os.linesep).join(lines)
        with open(self._path, 'w+') as fp:
            fp.write(text)

    def make_config(self, path, name):
        '''make config'''
        pelicanconf = import_module(name, path)
        return pelicanconf

    def __getattr__(self, key):
        return self.get(key)

    def __setattr__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)
