# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Alexis Métaireau'
SITENAME = "Alexis' log"
SITEURL = 'http://blog.notmyidea.org'
TIMEZONE = "Europe/Paris"
DEFAULT_LANG = 'en'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

GITHUB_URL = 'http://github.com/ametaireau/'
DISQUS_SITENAME = "blog-notmyidea"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
# DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
# DATE_FORMATS = {
#     'en': '%a, %d %b %Y'
# }

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('Biologeek', 'http://biologeek.org'),
         ('Filyb', "http://filyb.info/"),
         ('Libert-fr', "http://www.libert-fr.com"),
         ('N1k0', "http://prendreuncafe.com/blog/"),
         ('Tarek Ziadé', "http://ziade.org/blog"),
         ('Zubin Mithra', "http://zubin71.wordpress.com/"),)

SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
          ('lastfm', 'http://lastfm.com/user/akounet'),
          ('github', 'http://github.com/ametaireau'),)

# global metadata to all the contents
DEFAULT_METADATA = {'yeah': 'it is'}

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'pictures',
    'extra/robots.txt',
    ]

# custom page generated with a jinja2 template
TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"

DEFAULT_CATEGORY = 'misc'

PATH = 'content'
# Pelican_manager setting
SERVER_PORT = 5000
SERVER_DEBUG = True

# 后台管理的字段
# id and file_path and action 为默认的， 不可更改
# SERVER_FIELD_DEFAULT = {'sort': True, 'align': 'center', 'show': True}
SERVER_FIELD = {
    'title': {'sort': False, 'align': 'left', 'text': '标题', 'show': True},
    'author': {'sort': True, 'align': 'center', 'text': '作者'},
    'date': {'text': '时间'},
    'modified': {'text': '修改时间'},
    'category': {'text': '分类'},
    'status': {'text': '状态'},
}

# 页面分页条数
PAGE_SIZE = 10
PAGE_HIDE_COLUMN = ['path']

# 文章标题的颜色是否和 Status 对应
TITLE_COLOR_WITH_STATUS = True
# 当 TITLE——TITLE_COLOR_WITH_STATUS 为 True 时才起作用
TITLE_COLOR_WITH_STATUS_IS_PUBLISHED = 'success'
TITLE_COLOR_WITH_STATUS_IS_DRAFT = 'danger'

# 翻译软件名称, (youdao, baidu, google)
TRANSLATE_NAME = 'youdao'

# 有道翻译 API
TRANSLATE_APP_ID = ''
TRANSLATE_APP_KEY = ''
