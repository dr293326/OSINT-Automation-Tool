import subprocess


def exec_command(tool_name, parameters):
    split_list = parameters.split()
    split_list.insert(0, tool_name)
    result = subprocess.run(split_list, stdout=subprocess.PIPE, check=True)
    if result.returncode != 0:
        return ''
    else:
        return result.stdout.decode('utf-8')
    # return subprocess.run(split_list, stdout=subprocess.PIPE).stdout.decode('utf-8')


class SystemToolsManager:
    x = 0

    def __init__(self, x):
        self.x = x

    def nmap(self,params):
        self.x = 0
        exec_command('nmap', params)

    def the_harvester(self):
        self.x = 0
        exec_command('theHarvester', '')

    def recon_ng(self):
        self.x = 0
        exec_command('recon_ng', '')
