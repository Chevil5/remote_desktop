import argparse
from InfrastructureHandler import InfrastructureHandler

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--action',
                    choices=['init', 'install_vm', 'run_vm'],
                    help='Action it is basic argument witch set main goal of running script',
                    required=True
                    )

parser.add_argument('-r', '--ram', type=int, help='RAM of a new machine')
parser.add_argument('-hd', '--hdd', type=int, help='HDD of a new machine')
parser.add_argument('-o', '--os', choices=['ubuntu'], type=str, help='Operation system of a new machine')

args = vars(parser.parse_args())
infrastructure_obj = InfrastructureHandler()


if args.get('action') == 'init':
    infrastructure_obj.init()


if args.get('action') == 'install_vm':
    # print(args.get('os'), args.get('ram'), args.get('hdd'))
    vnc_ip = infrastructure_obj.install_vm(args.get('os'), args.get('ram'), args.get('hdd'))
    print(vnc_ip)
