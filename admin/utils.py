import os, sys

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
def make_path(generate):
    ''' 组装path'''
    all_files = []
    for root, dirs, files in generate:
        if files:
            for file_ in files:
                all_files.append(os.path.join(root, file_))

    return all_files
