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
                ['apt-get', 'install', 'virtualbox', '-y'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            out, er = instalation_proc.communicate()
            instalation_proc
            print(out)
        else:
            print('VMBOX is installed')
