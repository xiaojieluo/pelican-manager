import markdown
import codecs
from markdown.extensions import meta
import sys
from admin.article import MarkdownArticle
import pytest

@pytest.fixture()
def article(request):
    path = "tests/articles/test.md"
    article = MarkdownArticle(path)
    return article

def test_use_article_model_to_parse_markdown_text(article):
    assert article.meta['title'] == 'This is title'

def test_use_article_model_to_update_metadata(article):
    status = 'draft'
    article.update_meta('status', status)
    article.save()
    assert article.meta['status'] == status
