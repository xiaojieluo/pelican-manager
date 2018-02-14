#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Xiaoji'
SITENAME = "llnhhy's Blog"
SITEURL = 'http://www.llnhhy.com'
PATH = 'content'
PELICANTOOL_PATH = 'content/posts'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

# 将 资源文件与文章文件混合在同一文件夹中
STATIC_PATHS = [
    'posts',
    'downloads',
    'extra/robots.txt',
    'extra/favicon.ico',
    ]
STATIC_SAVE_AS = 'posts/'
# ARTICLE_PATHS = ['posts']
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARTICLE_URL = 'posts/{slug}.html'

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': '/robots.txt'},
    }

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    # 'ipynb.markup',
    'sitemap',
    'googleplus_comments',
    'render_math',
    ]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes/abctheme_for_pelican'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'style.css'

# 主题设置
DESCRIPTION = "To be a Full Stack Engineer."
THEME_LINKS = (
                ('Archives', '/archives.html'),
                ('Links', '/links.html'),
                ('Tags', '/tags.html'),
                ('Github','http://www.github.com/xiaojieluo'),
                ('Linkedin','http://linkedin.com/'),)

# DEFAULT_DATE_FORMAT = '%B %d %Y'
DEFAULT_DATE_FORMAT = '%Y-%d-%b'
# 所在国家
COUNTRY = 'China'
# 所在城市
CITY = 'Nanjing'

GOOGLE_ANALYTICS = 'UA-92533917-1'
# 是否开启代码高亮
HIGHLIGHT = True
HIGHLIGHT_THEME = 'atom-one-light'

COMMENT_STATUS = True
COMMENT = 'disqus'

PAGE = (('Home', '/'),
        ('Archive', '/archives.html'),
        )

SITE = dict(
    title=SITENAME,
    description='llnhhy\'s Blog | Web | python | Code | Computer Sciences',
    copyright='<p>I’m <strong><a href="/about">LuoXiaojie</a></strong>, a web developer who contributes open-source projects. You are reading my <a href="http://www.llnhhy.com">blog</a> powered by <a href="https://blog.getpelican.com/">Pelican</a> and <a href="https://github.com/xiaojieluo/abctheme_for_pelican.git">abctheme</a>. All articles are under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a>. Follow me on <a href="https://twitter.com/xiaojieluo">Twitter</a> for communicating, <a href="https://github.com/Xiaojieluo">GitHub</a> for code, and <a href="https://www.instagram.com/geekplux">Instagram</a> for daily.</p>'
)


COPYRIGHT = '&copy; 2017-2018 Powered by <a href="https://blog.getpelican.com/" target="_blank">Pelican</a> Theme &copy; <a href="https://github.com/xiaojieluo" target="_blank">LuoXiaojie</a>'

TESTLIST = ['1', '2']
TESTDICT = {}
