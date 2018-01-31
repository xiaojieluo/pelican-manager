import sys, os
import imp
import toml
from .utils import import_module

class PelicanConfig(object):
    def __init__(self, path):
        self.path = path
        self.parse_config()

    def parse_config(self):
        '''parse pelican config
        '''
        self.pelicanconf = import_module('pelicanconf', self.path)

    def __getattr__(self, key):
        return self.__getitem__(key)

    def __getitem__(self, key):
        if self.__dict__.get(key, None) is None:
            try:
                return getattr(self.pelicanconf, key)
            except Exception as e:
                print(e)
                return None

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kw)
        return cls._instance

class Config(dict, Singleton):
    ''' pelican_manager config'''
    # _instance = None
    # def __new__(cls, *args, **kw):
    #     if not cls._instance:
    #         cls._instance = super(Config, cls).__new__(cls, *args, **kw)
    #     return cls._instance

    def __init__(self):
        dict.__init__(self, self.make_config())

    def filter_data(self, data):
        server = ['port', 'debug']
        blog = ['path']

        conf = {
            'server': {},
            'blog': {},
        }
        for key, value in data.items():
            if key in server:
                if key == 'debug':
                    value = bool(value)
                conf['server'][key] = value
            elif key in blog:
                conf['blog'][key] = value

        filter_conf = {k:v for k, v in conf.items() if v}
        return filter_conf

    def update(self, *args, **kw):
        data ={}
        if args:
            data.update(args[0])
        if kw:
            data.update(kw)

        new_config = self.filter_data(data)
        super().update(new_config)

    def save(self):
        ''' 将 config 写入当前工作目录的 pelican_manager.toml 文件中'''
        toml_string = toml.dumps(self)
        print("=====")
        print(toml_string)
        path = os.path.join(os.getcwd(), 'pelican_manager.toml')
        with open(path, 'w') as fp:
            fp.write(toml_string)

    def make_config(self):
        '''make config'''
        path = os.path.join(os.getcwd(), 'pelican_manager.toml')
        default = self.parse_toml()
        if os.path.exists(path):
            custom = self.parse_toml(path)
            default.update(custom)

        return default

    def parse_toml(self, path=None):
        '''从 filepath 中解析 toml 配置文件
        '''
        config = {}
        if path is None or not os.path.exists(path):
            path = os.path.join(os.path.dirname(__file__), './config/pelican_manager.toml')

        config.update(toml.load(path))
        return config
