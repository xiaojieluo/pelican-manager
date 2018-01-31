import markdown
import codecs
from markdown.extensions import meta
import sys
from pelican_manager.article import MarkdownArticle, article_factory, Article, InterfaceNotImpleteException
import pytest

@pytest.fixture()
def article(request):
    path = "tests/articles/test.md"
    article = article_factory(path)
    return article

def test_article_factory(article):
    assert type(article) == MarkdownArticle

def test_use_article_model_to_parse_markdown_text(article):
    assert article.meta['title'] == 'This is title'

def test_use_article_model_to_update_metadata(article):
    status = 'draft'
    result = article.update_meta('status', status)
    article.save()
    assert result is None
    assert article.meta['status'] == status

def test_article_update_meta(article):
    name = 'None'
    res = article.update_meta(name, 'Test_None')

    assert res == "不存在的 metadata:{}".format(name)


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
    path = "tests/articles/no_metadata.md"
    article = article_factory(path)
    assert article.meta == {}
