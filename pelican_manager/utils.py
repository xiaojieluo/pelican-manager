import os, sys
import random
import hashlib
import urllib
import requests
from pathlib import Path

def iterdir(path):
    '''从给定的 path 参数开始遍历目录
    返回生成器类型， root, files
    '''
    generate = os.walk(path)

    for root, dirs, files in generate:
        if files:
            for file_ in files:
                full_path = os.path.join(root, file_)
                p = full_path.replace(path, '')
                unipath = Path(p)
                name = unipath.parts
                if unipath.parts[0] == '/':
                    name = unipath.parts[1:]

                file_path = os.path.join(*name)
                # print(file_path)
                yield file_path


class Translate(object):
    def __init__(self, trans_name, appid, appkey):
        self.trans_name = trans_name
        self.appid = appid
        self.appkey = appkey
        self.salt = str(random.randint(1, 65536))

    def translate(self, source, from_='auto', to='en'):
        return {
            'youdao': self.youdao_translate(source, from_, to),
        }.get(self.trans_name, None)

    def youdao_translate(self, source, from_, to):
        '''有道翻译
        其中 self.appid = appKey
        '''
        sign = self.appid + source + self.salt + self.appkey
        sign = sign.encode('utf8')
        m1 = hashlib.md5()
        m1.update(sign)
        sign = m1.hexdigest()
        url = 'http://openapi.youdao.com/api'
        url = '{}?appKey={}&q={}&from={}&to={}&salt={}&sign={}'.format(url, self.appid,
                                urllib.parse.quote(source), from_, to, self.salt, sign)

        try:
            r = requests.get(url, timeout=3)
            r.encoding = 'utf-8'
            result = r.json()
            if 'translation' in result:
                return result['translation'][0]
            else:
                return None
        except Exception as e:
            print(e)
            return None


    def baidu_translate(self, source, from_, to):
        '''百度翻译'''
        pass

    def google_translate(self, source, from_, to):
        '''Google 翻译'''
        pass

def handle_duplicate_name(path, filename, start_index = 0):
    '''检测目录下是否有重名文件
    如果有的话， 在当前文件名后面递增数字
    '''
    if not os.path.exists(path):
        os.makedirs(path)

    full_path = ''
    if os.path.exists(os.path.join(path, filename)):
        new_name = filename.split('.')
        start_index += 1
        if len(new_name) == 2:
            new_name.insert(1, str(start_index))
        else:
            new_name[1] = str(start_index)
        full_path = handle_duplicate_name(path, '.'.join(new_name), start_index)
    else:
        full_path = os.path.join(path, filename)

    return full_path
