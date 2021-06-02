class VirusTotalResult:
    def __init__(self, dns_record_list, popularity_ranks_list, analysis_stats, analysis_results_list,
                 public_key, subdomains_list, subject, categories):
        self.dns_record_list = dns_record_list
        self.popularity_ranks_list = popularity_ranks_list
        self.analysis_stats = analysis_stats
        self.analysis_results_list = analysis_results_list
        self.public_key = public_key
        self.subdomains_list = subdomains_list
        self.subject = subject
        self.categories = categories

    def format_to_html(self):
        print('not implemented yet')
