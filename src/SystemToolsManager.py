import subprocess

from shodan import Shodan
from xml.etree import ElementTree
from data.NmapResult import NmapResult
from data.TheHarvesterResult import TheHarvesterResult
from data.ShodanResult import ShodanResult
from data.NmapResult import NmapResult
from data.TheHarvesterResult import TheHarvesterResult
from data.SpiderResult import SpiderResult
import requests
import json
import socket

from data.VirusTotalResult import VirusTotalResult


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


def virustotal(main_website_address):
    headers = {
        'x-apikey': '9360782e77bdb96caf0a6c459aa9d66006e639d59af2162b01e70af514c16d1b',
    }
    params = (
        ('query', main_website_address),
    )
    try:
        response = requests.get('https://www.virustotal.com/api/v3/search', headers=headers, params=params)
        return parse_virustotal_json_result(response.content.decode('utf-8'))
    except requests.exceptions.ConnectionError:
        print('VirusTotal API refused connection')
        return parse_virustotal_json_result('')


def shodanAPI(domain_ip):
    api = Shodan('Y2IXliQcbqyoAJyKynux1ovOjX5M2ukI')
    domain_ip = socket.gethostbyname(domain_ip)
    host = api.host(domain_ip)
    return ShodanResult(host['ip_str'], host.get('hostnames', 'n/a'), host.get('org', 'n/a'), host.get('os', 'n/a'),
                        host.get('asn', 'n/a'), host.get('domains', 'n/a'), host.get('ports', 'n/a'),
                        host.get('country_name', 'n/a'),
                        host.get('city', 'n/a'), host.get('latitude', 'n/a'), host.get('longitude', 'n/a'))


def parse_spider_json_result(result):
    result_json = json.loads(result)
    result = []
    types = ["Email Address", "Open TCP Port Banner"]
    for obj in result_json:
        if obj['type'] in types:
            result.append(obj['data'])
    return result


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
        if extra is not None:
            extraports.append(dict([('state', extra.get('state')), ('count', extra.get('count'))]))

    for port in host.find('ports').findall('port'):
        if port is not None:
            protocol = port.get('protocol')
            port_id = port.get('portid')
            port_state = port.find('state').get('state')
            service_name = port.find('service').get('name')
            ports.append(dict([('protocol', protocol), ('port_id', port_id), ('port_state', port_state),
                               ('service_name', service_name)]))
    summary = root.find('runstats').find('finished').get('summary')
    return NmapResult(state, host_ip_address, ip_version, hostnames, extraports, ports, summary)


def parse_harvester_xml_result2(xml_string):
    emails_list = []
    hosts_list = []

    root = ElementTree.fromstring(xml_string)
    mails = root.findall('email')
    hosts = root.findall('host')

    for x in mails:
        if x is not None:
            emails_list.append(x.text)

    for x in hosts:
        if x is not None:
            var1 = x.find('ip')
            var2 = x.find('hostname')
            if (var1 is not None) and (var2 is not None):
                hosts_list.append(dict([('ip', var1.text), ('hostname', var2.text)]))

    return TheHarvesterResult(emails_list, hosts_list)


def parse_virustotal_json_result(json_string):
    root = json.loads(json_string)
    root = root['data'][0]['attributes']

    last_dns_records = root['last_dns_records']
    popularity_ranks = root['popularity_ranks']
    last_analysis_stats = root['last_analysis_stats']
    last_analysis_results = root['last_analysis_results']
    public_key = root['last_https_certificate']['public_key']
    subdomains = root['last_https_certificate']['extensions']['subject_alternative_name']
    subject = root['last_https_certificate']['subject']
    categories = root['categories']

    return VirusTotalResult(dns_record_list=last_dns_records, popularity_ranks_list=popularity_ranks,
                            analysis_stats=last_analysis_stats, analysis_results_list =last_analysis_results,
                            public_key=public_key, subject=subject, subdomains_list=subdomains,
                            categories=categories)


# def find_list_element_by_name(curr_list, name):
#     iter = 0
#     for elem in curr_list:
#         if elem[0] == name:
#             return iter
#         iter = iter + 1
#     return -1
