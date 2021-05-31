class NmapResult:

    def __init__(self, host_status, ip_address, ip_type, host_names, extraports, ports, summary):
        self.host_status = host_status
        self.ip_address = ip_address
        self.ip_type = ip_type
        self.host_names = host_names
        self.extraports = extraports
        self.ports = ports
        self.summary = summary

    def format_to_html(self):
        print('not implemented yet')