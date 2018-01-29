import sys, os
import imp

class Config(object):
    def __init__(self, path):
        self.path = path
        self.parse_config()

    def parse_config(self):
        '''parse pelican config
        '''
        self.pelicanconf = self.import_module('pelicanconf', self.path)

    def __getattr__(self, key):
        if self.__dict__.get(key, None) is None:
            try:
                return getattr(self.pelicanconf, key)
            except Exception as e:
                print(e)
                return None

    def import_module(self, name, path):
        ''' import module'''
        base_dir = os.path.dirname(path)
        try:
            fp, pathname, description = imp.find_module(name, [base_dir])
            return imp.load_module(name, fp, pathname, description)
        except Exception as e:
            print(e)

class Args(object):
    '''存储命令行参数的类
    server: int 运行端口
    debug: bool 是否开启调试
    path: 存放文章的目录
    '''
    def __init__(self):
        pass

    def __getattr__(self, key):
        if key == 'path':
            return 'tests/articles'
