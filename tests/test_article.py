import markdown
import codecs
from markdown.extensions import meta
import sys
from pelican_manager.article import MarkdownArticle, article_factory, Article, InterfaceNotImpleteException
import pytest
import os

@pytest.fixture()
def article(request):
    path = "tests/content/article_with_metadata_and_contents.md"
    article = article_factory(path)
    return article

def test_article_factory(article):
    markdown = ['.md', '.markdown']
    rst = ['.rst']
    _,ext = os.path.splitext(article.path)
    if ext in markdown:
        assert type(article) == MarkdownArticle

def test_parse_markdown(article):
    assert article.meta['title'] is not None

def test_use_article_model_to_update_metadata(article):
    status = 'draft'
    article.update_meta('status', status)
    article.save()
    assert article.meta['status'] == status

def test_article_update_meta():
    article = article_factory('tests/content/no_metadata.md')
    name = 'None'
    article.update_meta(name, 'Hello')
    article.update_meta('Status', 'published')
    article.update_meta('Author', 'Xiaojie Luo')
    article.save()

    assert article.meta['status'] ==  'published'
    assert article.meta['author'] == 'Xiaojie Luo'

@pytest.fixture()
def TestArticle(request):
    class TestArticle(Article):
        pass
    return TestArticle

def test_article_make_parser_raise_exception(TestArticle):
    with pytest.raises(InterfaceNotImpleteException):
        test_article = TestArticle(None)

def test_article_parse_text_raise_exception():
    class TestArticle(Article):
        def make_parser(self):
            pass
    test_article = TestArticle(None)
    with pytest.raises(InterfaceNotImpleteException):
        test_article.parse_text()

    with pytest.raises(InterfaceNotImpleteException):
        test_article.update_meta('k', 'v')

def test_parse_no_metadata_article():
    path = "tests/content/article_without_metadata.md"
    article = article_factory(path)
    assert article.meta == {}
