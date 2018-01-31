import argparse
import sys, os
from pelican_manager import make_app
import toml
from pelican_manager.config import Config
# from .utils import make_config


def parse_args(args):
    ''' parse args'''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-p', '--port', nargs='?', type=int)

    args = parser.parse_args()
    return args


def main():
    '''enter'''
    # config = make_config()
    config = Config()
    args = parse_args(sys.argv[1:])
    app = make_app()
    app.run(
        port=args.port or config['server']['port'],
        )

if __name__ == '__main__':
    main()
