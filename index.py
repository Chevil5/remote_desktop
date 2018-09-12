import argparse
from InfrastructureHandler import InfrastructureHandler

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--action', choices=['init', 'install', 'run'])

args = vars(parser.parse_args())

if args.get('action') == 'init':
    i = InfrastructureHandler()
    i.init()
