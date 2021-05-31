import subprocess
from shodan import Shodan


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
    
    def shodanAPI(self, domainIP):
        self.x = 0
        api = Shodan('Y2IXliQcbqyoAJyKynux1ovOjX5M2ukI') # API account key, required to use shodan
        host = api.host(domainIP) # return a lot of data, stored in JSON type
        print("""
                Basic information:
                IP: {}
                Hostname: {}
                Organization: {}
                Operating System: {}
                AS number: {}
                Domains: {}
                Ports: {}
        """.format(host['ip_str'], host.get('hostnames','n/a'), host.get('org', 'n/a'), host.get('os', 'n/a'), host.get('asn', 'n/a'), host.get('domains','n/a'), host.get('ports','n/a')))
    
    def spiderfoot(self, pageName, modules)
        self.x = 0
        params = 'spiderfoot -s' + pageName + '-t' + modules + '-f -q -o json'
        exec_command('spiderfoot', params)
        
