import subprocess

from shodan import Shodan
from xml.etree import ElementTree
from data.NmapResult import NmapResult
from data.ShodanResult import ShodanResult


def exec_command(tool_name, parameters):
    split_list = parameters.split()
    split_list.insert(0, tool_name)
    result = subprocess.run(split_list, stdout=subprocess.PIPE, check=True)
    if result.returncode != 0:
        return ''
    else:
        return result.stdout.decode('utf-8')
    # return subprocess.run(split_list, stdout=subprocess.PIPE).stdout.decode('utf-8')


def nmap(params):
    return exec_command('nmap', params)


def the_harvester(params):
    return exec_command('theHarvester', params)


def recon_ng(params):
    return exec_command('recon_ng', params)


def spiderfoot(params):
    return exec_command('spiderfoot', params)


def parse_nmap_xml_result(xml_string):
    hostnames = []
    extraports = []
    ports = []

    root = ElementTree.fromstring(xml_string)
    host = root.find('host')

    state = host.find('status').get('state')
    host_ip_address = host.find('address').get('addr')
    ip_version = host.find('address').get('addrtype')

    for hostname in host.find('hostnames').findall('hostname'):
        hostnames.append(hostname.get('name'))

    for extra in host.find('ports').findall('extraports'):
        extraports.append(dict([(state, extra.get('state')), ('count', extra.get('count'))]))

    for port in host.find('ports').findall('port'):
        protocol = port.get('protocol')
        port_id = port.get('portid')
        port_state = port.find('state').get('state')
        service_name = port.find('service').get('name')
        ports.append(dict([('protocol', protocol), ('port_id', port_id), ('port_state', port_state),
                           ('service_name', service_name)]))
    summary = root.find('runstats').find('finished').get('summary')
    return NmapResult(state, host_ip_address, ip_version, hostnames, extraports, ports, summary)


def shodanAPI(domain_ip):
    api = Shodan('Y2IXliQcbqyoAJyKynux1ovOjX5M2ukI')
    host = api.host(domain_ip)
    return ShodanResult(host['ip_str'], host.get('hostnames', 'n/a'), host.get('org', 'n/a'), host.get('os', 'n/a'),
                        host.get('asn', 'n/a'), host.get('domains', 'n/a'), host.get('ports', 'n/a'), host.get('country_name', 'n/a'),
                        host.get('city', 'n/a'), host.get('latitude', 'n/a'), host.get('longitude', 'n/a'))
