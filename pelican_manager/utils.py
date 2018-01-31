import os, sys
import toml
import imp

def import_module( name, path):
    '''动态加载模块
    '''
    base_dir = os.path.dirname(path)
    try:
        fp, pathname, description = imp.find_module(name, [base_dir])
        return imp.load_module(name, fp, pathname, description)
    except Exception as e:
        print(e)
        return None

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

# def make_path(generate):
#     ''' 组装path'''
#     all_files = []
#     for root, dirs, files in generate:
#         if files:
#             for file_ in files:
#                 all_files.append(os.path.join(root, file_))
#
#     return all_files


# def parse_toml(path = None):
#     '''从 filepath 中解析 toml 配置文件
#     '''
#     config = {}
#     if path is None or not os.path.exists(path):
#         # path = os.path.join(os.getcwd(), './config/pelican_manager')
#         path = os.path.join(os.path.dirname(__file__), './config/pelican_manager.toml')
#         config.update(toml.load(path))
#     return config

# def make_config():
#     path = os.path.join(os.getcwd(), 'pelican_manager.toml')
#     default = parse_toml()
#     if os.path.exists(path):
#         default.update(parse_toml(path))
#
#     return default
