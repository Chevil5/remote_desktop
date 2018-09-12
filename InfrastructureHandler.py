import os
import subprocess


class InfrastructureHandler:
    def init(self):
        vb_instalation_checking = subprocess.Popen(
            ["dpkg", "--get-selections", "virtualbox"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        installed, noninstalled = vb_instalation_checking.communicate()
        if noninstalled:
            instalation_proc = subprocess.Popen(
                ['sudo', '-S', 'apt-get', 'install', 'virtualbox', '-y'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            print(instalation_proc.communicate('7753191\n'))
            out, er = instalation_proc.communicate()
            print(out)
        else:
            print('VMBOX is installed')
