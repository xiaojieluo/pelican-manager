import markdown
import codecs
from markdown.extensions import meta
import sys
from pelican_manager.article import MarkdownArticle, article_factory, Article, InterfaceNotImpleteException
import pytest
import os
from pelican_manager.utils import iterdir


TEST_ARTICLES_LIST = [k for k in iterdir("tests/content")]

@pytest.fixture(params=TEST_ARTICLES_LIST)
def article(request):
    path = request.param
    article = article_factory(path)
    if article:
        return article

def test_article_factory(article):
    markdown = ['.md', '.markdown']
    rst = ['.rst']
    if article:
        _,ext = os.path.splitext(article.path)
        if ext in markdown:
            assert type(article) == MarkdownArticle
