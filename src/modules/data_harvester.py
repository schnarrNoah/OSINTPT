"""
Methoden:
    fetch_domains(target): Sammelt Domains zu einem Ziel.
    fetch_emails(target): Extrahiert E-Mail-Adressen.
    fetch_ip_addresses(target): Sammelt IP-Adressen.
    shodan(api_key, target): Nutzt die Shodan-API für Detailanalysen.
"""

class DataHarvester:

    def __init__(self):
        # SHODAN --------------------------------------------------------------------------------
        self.search_shodan('shodan_api_key', '')

        # HAVE I BEEN PWNED ---------------------------------------------------------------------
        self.check_email_pwned('e@x.com')

        # VIRUSTOTAL ----------------------------------------------------------------------------
        self.check_file_with_virustotal('dein_virustotal_api_key', 'hash_of_the_file')
