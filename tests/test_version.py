from pelican_manager import __version__ as version

def test_version():
    attrs = ['__title__', '__description__', '__url__', '__version__',
            '__build__', '__author__', '__author_email__', '__license__',
            '__copyright__', '__cake__']

    for attr in attrs:
        assert attr in version.__dir__()
