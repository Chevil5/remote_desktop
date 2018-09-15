import argparse
from InfrastructureHandler import InfrastructureHandler

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--action',
                    choices=['init', 'install_vm', 'run_vm'],
                    help='Action it is basic argument witch set main goal of running script',
                    required=True
                    )

args = vars(parser.parse_args())

if args.get('action') == 'init':
    i = InfrastructureHandler()
    i.init()
