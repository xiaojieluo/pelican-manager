import os, sys
import imp

class NotFoundPelicanConfig(Exception):
    pass

def import_module( name, path):
    '''动态加载模块
    '''
    base_dir = os.path.dirname(path)
    try:
        fp, pathname, description = imp.find_module(name, [base_dir])
        return imp.load_module(name, fp, pathname, description)
    except ImportError as e:
        info = '无法导入 {} 模块！\n{} 文件不存在\n请检查路径后重试， 或用 -c 参数重新指定 pelican 配置文件'.format(name, path)
        raise NotFoundPelicanConfig(info)
        exit()

def traversal(path):
    '''从给定的 path 参数开始遍历， 提取出所有后缀为 .md 的文件
    返回生成器类型， root, files
    '''
    generate = os.walk(path)
    for root, dirs, files in generate:
        if files:
            for file_ in files:
                full_path = os.path.join(root, file_)
                yield full_path
