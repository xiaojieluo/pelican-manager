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

@pytest.fixture()
def TestArticle(request):
    class TestArticle(Article):
        pass
    return TestArticle

def test_article_parse_text_raise_exception():
    class TestArticle(Article):
        def make_parser(self):
            pass
    test_article = TestArticle(None)

    with pytest.raises(InterfaceNotImpleteException):
        test_article.update_meta('k', 'v')



# test new article
def test_article_not_exists():
    path = 'tests/content/article_not_exists.md'
    article = article_factory(path)
    article.update_meta('title', 'article not exists')
    article.text = 'hello'
    article.save()

    assert article.meta['title'] == 'article not exists'
    assert article.text == 'hello'
    assert os.path.exists(path) is True

    os.remove(path)

def test_markdown_article():
    path = 'tests/content/article_with_metadata.md'
    article = article_factory(path)

    assert article.meta
    assert article.text
