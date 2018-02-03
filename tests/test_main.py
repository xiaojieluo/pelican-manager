from pelican_manager import __main__ as main

def test_parse_args():
    args = ['-p', '4000']
    parse = main.parse_args(args)

    assert parse.port == 4000
