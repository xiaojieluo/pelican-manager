import argparse
import sys, os
from pelican_manager import make_app
from pelican_manager.config import Config


def parse_args(args):
    ''' parse args'''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-p', '--port', nargs='?', type=int)
    parser.add_argument('-c', '--config', nargs='?', type=str)

    args = parser.parse_args(args)
    return args


def main():
    '''enter'''
    args = parse_args(sys.argv[1:])
    app = make_app(args.config)
    config = Config()
    app.run(
        port=args.port or config.server_port,
        )

if __name__ == '__main__':
    main()
