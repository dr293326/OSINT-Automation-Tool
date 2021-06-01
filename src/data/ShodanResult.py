def list_to_str(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)
    return str1


def check_if_none(var):
    if var is None:
        return "Not found"
    else:
        return var


class ShodanResult:

    def __init__(self, ip_address, hostname, org, op_system, as_num, domains, ports, country, city, latitude, longitude):
        self.ip_address = check_if_none(ip_address)
        self.hostname = check_if_none(hostname)
        self.org = check_if_none(org)
        self.op_system = check_if_none(op_system)
        self.as_num = check_if_none(as_num)
        self.domains = check_if_none(domains)
        self.ports = check_if_none(ports)
        self.country = check_if_none(country)
        self.city = check_if_none(city)
        self.latitude = check_if_none(latitude)
        self.longitude = check_if_none(longitude)

    def format_to_html(self):
        htmlFile = "<br><h3>SHODAN</h3><br><table><tr><th>Key</th><th>Value</th></tr>"
        htmlFile = htmlFile + "<tr><td>IP Address:</td><td>" + self.ip_address + "</td></tr>"
        htmlFile = htmlFile + "<tr><td>Hostname:</td><td>" + list_to_str(self.hostname) + "</td></tr>"
        htmlFile = htmlFile + "<tr><td>Organization:</td><td>" + self.org + "</td></tr>"
        htmlFile = htmlFile + "<tr><td>Operating system:</td><td>" + self.op_system + "</td></tr>"
        htmlFile = htmlFile + "<tr><td>AS Number:</td><td>" + self.as_num + "</td></tr>"
        htmlFile = htmlFile + "<tr><td>Domains:</td><td>" + list_to_str(self.domains) + "</td></tr>"
        htmlFile = htmlFile + "<tr><td>Ports:</td><td>" + list_to_str(self.ports) + "</td></tr>"
        htmlFile = htmlFile + "<tr><td>Country:</td><td>" + self.country + "</td></tr>"
        htmlFile = htmlFile + "<tr><td>City:</td><td>" + self.city + "</td></tr>"
        htmlFile = htmlFile + "<tr><td>Latitude:</td><td>" + str(self.latitude) + "</td></tr>"
        htmlFile = htmlFile + "<tr><td>Longitude:</td><td>" + str(self.longitude) + "</td></tr>"
        htmlFile = htmlFile + "</table><br>"
        return htmlFile
