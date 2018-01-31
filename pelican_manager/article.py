import markdown
import codecs
import re, os

class InterfaceNotImpleteException(Exception):
    pass

def article_factory(path):
    markdown = ['.md', '.markdown']
    rst = ['.rst']

    _, ext = os.path.splitext(path)
    if ext in markdown:
        return MarkdownArticle(path)
    # else:
    #     return


class Article(object):
    ''' article model
    传入一片文章， 读取出 metadata
    '''
    def __init__(self, path):
        self.path = path
        self.parser = self.make_parser()
        self._text = None

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
        super().__init__( path)
        self._meta = None

    @property
    def meta(self):
        if self._meta is None:
            self.parse_text()
        return self._meta

    def make_parser(self):
        return markdown.Markdown(extensions=['markdown.extensions.meta'])

    def parse_text(self):
        input_file = codecs.open(self.path, mode='r', encoding='utf-8')
        text = input_file.read()
        self.html = self.parser.convert(text)
        self._meta = self._parse_meta()
        return text

    def _parse_meta(self):
        ''' parser meta data.
        返回处理后的 meta data
        '''
        try:
            meta = self.parser.Meta
        except Exception as e:
            print("=========={}=============".format(self.path))
            print("{} => Catch error:{}".format(self.path, e))
            meta = {}
        finally:
            new_meta = {k: v[0] for k, v in meta.items()}
            return new_meta

    def update_meta(self, name, value):
        ''' 更新 metadata , 并写回文件中
        Args:
            name: str, 指定 meta 的 名称， 部分大小写， 程序会自动转换成开头大写的单词写入文件中
            value: 要更新成的值
        '''
        name = name.capitalize()
        META_RE = re.compile('^[ ]{0,3}(?P<key>['+name+']+):\s*(?P<value>.*)')
        END_RE = re.compile(r'^(-{3}|\.{3})(\s.*)?')
        lines = self.text.split('\n')
        match = None
        while lines:
            line = lines.pop(0)
            m1 = META_RE.match(line)
            if line.strip() == '' or END_RE.match(line):
                break;
            if m1:
                match = m1
                break;
        if match:
            self.text = self.text.replace(match.group(2), value)
        else:
            return "不存在的 metadata:{}".format(name)

    def save(self):
        ''' 保存更改并更新缓存
        '''
        with open(self.path, 'w') as fp:
            fp.seek(0, 0)
            fp.write(self.text)
        self.parse_text()
