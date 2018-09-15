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
            subprocess.call(['sudo -S apt-get', 'install', 'virtualbox', '-y'])
        else:
            print('VMBOX is installed')

    def install_vm(self, os, ram, hdd):
        if os == 'ubuntu':

            subprocess.call(['vboxmanage', 'createvm', '--name', 'UbuntuTest', '--ostype', 'Ubuntu_64', '--register'])
            subprocess.call(['vboxmanage', 'modifyvm', 'UbuntuTest', '--cpus', '1', '--memory', str(ram), '--nic1', 'nat',
                             '--boot1', 'dvd'])
            subprocess.call(['vboxmanage', 'createmedium', 'disk',
                             '--filename', '/home/chevil/VirtualBox VMs/UbuntuTest/ubuntu1604.vdi', '--size', str(hdd)])
            subprocess.call(['vboxmanage', 'storagectl', 'UbuntuTest', '--name', 'SATA', '--add', 'sata'])
            subprocess.call(['vboxmanage', 'storageattach', 'UbuntuTest', '--storagectl', 'SATA', '--port', '0', '--device',
                             '0', '--type', 'hdd', '--medium', '/home/chevil/VirtualBox VMs/UbuntuTest/ubuntu1604.vdi'])

            subprocess.call(['vboxmanage', 'storageattach', 'UbuntuTest', '--storagectl', 'SATA', '--port', '1', '--device',
                             '0', '--type', 'dvddrive',
                             '--medium', '/home/chevil/VirtualBox VMs/ubuntu-18.04.1-desktop-amd64.iso'])

        subprocess.call(['vboxmanage', 'modifyvm', 'UbuntuTest', '--vrde', 'on'])
        subprocess.call(['vboxmanage', 'modifyvm', 'UbuntuTest', '--vrdeaddress', '127.0.0.1'])
        subprocess.call(['vboxmanage', 'modifyvm', 'UbuntuTest', '--vrdeport', '5901'])
        subprocess.call(['vboxmanage', 'modifyvm', 'UbuntuTest', '--vrdeproperty', 'VNCPassword=12345678'])
        subprocess.call(['vboxmanage', 'startvm', 'UbuntuTest'])

        return 'http://127.0.0.1:8000'


