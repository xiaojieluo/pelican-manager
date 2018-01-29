import pytest
from pelican_manager.utils import traversal

def test_traversal_all_markdown_files():
    path = 'tests/articles'
    ps = traversal(path)
    for floder, files in ps:
        print("{} => {}".format(floder, files))
