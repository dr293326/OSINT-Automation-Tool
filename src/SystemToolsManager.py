import subprocess

from shodan import Shodan
from xml.etree import ElementTree
from src.data.NmapResult import NmapResult
from src.data.TheHarvesterResult import TheHarvesterResult
import requests
import json

from src.data.VirusTotalResult import VirusTotalResult


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


def parse_harvester_xml_result(xml_string):
    emails_list = []
    hosts_list = []

    root = ElementTree.fromstring(xml_string)
    mails = root.findall('email')
    hosts = root.findall('host')

    for x in mails:
        emails_list.append(x.text)

    for x in hosts:
        hosts_list.append([('ip', x.find('ip').text), ('hostname', x.find('hostname').text)])

    return TheHarvesterResult(emails_list, hosts_list)


def shodanAPI(domainIP):
    api = Shodan('Y2IXliQcbqyoAJyKynux1ovOjX5M2ukI')  # API account key, required to use shodan
    host = api.host(domainIP)  # return a lot of data, stored in JSON type
    print("""
            Basic information:
            IP: {}
            Hostname: {}
            Organization: {}
            Operating System: {}
            AS number: {}
            Domains: {}
            Ports: {}
    """.format(host['ip_str'], host.get('hostnames', 'n/a'), host.get('org', 'n/a'), host.get('os', 'n/a'),
               host.get('asn', 'n/a'), host.get('domains', 'n/a'), host.get('ports', 'n/a')))


def spiderfoot(pageName, modules):
    params = 'spiderfoot -s' + pageName + '-t' + modules + '-f -q -o json'
    exec_command('spiderfoot', params)


def virustotal(main_website_address):
    headers = {
        'x-apikey': '9360782e77bdb96caf0a6c459aa9d66006e639d59af2162b01e70af514c16d1b',
    }
    params = (
        ('query', main_website_address),
    )
    response = requests.get('https://www.virustotal.com/api/v3/search', headers=headers, params=params)
    return parse_virustotal_json_result(response.content.decode('utf-8'))


def parse_virustotal_json_result(json_string):
    root = json.loads(json_string)
    last_dns_records = root['attributes']['last_dns_records']
    popularity_ranks = root['attributes']['popularity_ranks']
    last_analysis_stats = root['attributes']['last_analysis_stats']
    last_analysis_results = root['attributes']['last_analysis_results']
    public_key = root['attributes']['last_http_certificate']['public_key']
    subdomains = root['attributes']['last_http_certificate']['extensions']['subject_alternative_name']
    subject = root['attributes']['last_http_certificate']['subject']
    categories = root['attributes']['categories']

    return VirusTotalResult(dns_records=last_dns_records, popularity_ranks=popularity_ranks,
                            analysis_stats=last_analysis_stats, analysis_results=last_analysis_results,
                            public_key=public_key, subdomains_list=subdomains, subject=subject, categories=categories)
