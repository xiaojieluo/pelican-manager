import markdown
import codecs
import re, os
from pelican_manager.utils import handle_duplicate_name
from pelican_manager.config import Config

config = Config()

class InterfaceNotImpleteException(Exception):
    pass

class NotSupportFormat(Exception):
    pass

def article_factory(path):
    markdown = ['.md', '.markdown']
    rst = ['.rst']

    _, ext = os.path.splitext(path)
    if ext in markdown:
        return MarkdownArticle(path)
    else:
        return None


class Article(object):
    ''' article model
    传入一片文章， 读取出 metadata
    '''
    def __init__(self, path):
        self.path = path
        self.parser = self.make_parser()
        self._text = None # list
        self._raw_text = None #  去除 meta 的内容


    @property
    def full_path(self):
        ''' 返回文章的完整目录'''
        full_path = os.path.join(config.path or '', self.path)
        return full_path

    @property
    def text(self):
        '''
        返回纯文本格式的内容, 返回为列表类型， 包含两部分， metadata 与 content
        '''
        if self._text is None:
            self._text = self.parse_text()
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def make_parser(self):
        ''' 构造解析器: must'''
        raise InterfaceNotImpleteException("Interface Not Implete.")

    def parse_text(self):
        ''' 解析文章'''
        raise InterfaceNotImpleteException("Interface Not Implete.")

    def update_meta(self, name, value):
        ''' 更新 article 的 metadata
        Args:
            name: meta name,
            value: meta data
        '''
        raise InterfaceNotImpleteException("Interface Not Implete")



class MarkdownArticle(Article):
    '''解析 markdown 格式的文章'''

    def __init__(self, path):
        super().__init__( path )
        self._meta = None
        self._text = ''
        self.parse()

    def exists(self):
        ''' 判断文章是否存在'''
        if os.path.exists(self.full_path):
            return True
        return False

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, value):
        self._meta = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def update_meta(self, key, value):
        ''' 更新 meta'''
        self._meta[key] = value

    def save(self):
        '''保存更改
        # if os.path.exists(self.path):
        #
        '''
        path, filename = os.path.split(self.full_path)
        if not os.path.exists(path):
            os.makedirs(path)
        content = self.content
        with open(self.full_path, 'w') as fp:
            fp.seek(0, 0)
            fp.write(content)


    @property
    def content(self):
        '''返回完整内容
        '''
        contents = list()
        for key, value in self.meta.items():
            line_str = '{}: {}'.format(key.capitalize(), value)
            contents.append(line_str)
        contents.append('---')
        contents.append(self.text)
        content = '{}'.format(os.linesep).join(contents)
        return content

    def make_parser(self):
        return markdown.Markdown(extensions=['markdown.extensions.meta'])

    def parse(self):
        '''
        parse article.
        when self.path is not exists , raise FileNotFoundError exception.
        '''
        meta = {}
        text = ''
        if os.path.exists(self.full_path):
            input_file = codecs.open(self.full_path, mode='r', encoding='utf-8')
            text = input_file.read()
            meta = self._parse_meta(text)
            meta_split = self.meta_split(text)
            lines = text.split('\n')
            for line in lines:
                meta_split = self.get_meta_split(line)
                if meta_split:
                    index = lines.index(meta_split)
                    text = '\n'.join(lines[index+1:])
                    break
        self._meta = meta
        self.text = text

    def _parse_meta(self, text):
        ''' parser meta data.
        返回处理后的 meta data
        '''
        parser = markdown.Markdown(extensions=['markdown.extensions.meta'])
        try:
            parser.convert(text)
            meta = parser.Meta
        except Exception as e:
            print("=========={}=============".format(self.full_path))
            print("{} => Catch error:{}".format(self.full_path, e))
            meta = {}
        finally:
            new_meta = {k: v[0] for k, v in meta.items()}
            return new_meta

    def get_meta_split(self, line):
        END_RE = re.compile(r'(-{3,}|\.{3,})(\s.*)?')
        meta_split = ''
        end = END_RE.match(line)
        if end:
            return end.group(0)

    def meta_split(self, text):
        ''' 获取 metadata 与正文的分隔符'''
        END_RE = re.compile(r'(-{3,}|\.{3,})(\s.*)?')
        meta_split = ''
        lines = text.split('\n')
        for line in lines:
            end = END_RE.match(line)
            if end:
                meta_split = end.group(0)

        return meta_split

    def _create_file(self, path, content):
        '''
        创建文件
        Args:
            path : string, 文件的全路径， 包含文件名
            content: 要写入的内容
        '''
        # 递归创建目录
        full_path = handle_duplicate_name(*os.path.split(path))

        with open(full_path, 'w+') as fp:
            fp.write(content)
