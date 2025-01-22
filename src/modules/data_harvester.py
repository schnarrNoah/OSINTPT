import requests
import src.utils.api_utils as api

class DataHarvester:

    def __init__(self):
        """
        Initialisiert den DataHarvester und überprüft API-Verbindungen.
        """
        api.init_api_conn()

    def search_shodan(self, query):
        """
        Führt eine Shodan-Suche durch.
        """
        if api.ensure_shodan_connection():
            try:
                results = api.connections['shodan'].search(query)
                for result in results['matches']:
                    print(f"IP-Adresse: {result['ip_str']}")
                    print(f"Port: {result['port']}")
                    print(f"Organisation: {result.get('org', 'N/A')}")
                    print(f"Geolocation: {result.get('location', 'N/A')}")
                    print(f"Service: {result.get('product', 'N/A')}")
                    print("-" * 50)
            except Exception as e:
                print(f"Fehler bei der Shodan-Abfrage: {e}")

    def check_email_pwned(self, email):
        """
        Überprüft, ob eine E-Mail in der HIBP-Datenbank gefunden wurde.
        """
        if not api.connections['hibp']:
            print("HIBP-API-Key fehlt. Verbindung kann nicht hergestellt werden.")
            return

        url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
        headers = {
            'User-Agent': 'OSINT-Tool',
            'hibp-api-key': api.connections['hibp'],
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f"E-Mail {email} wurde in folgenden Datenschutzverletzungen gefunden:")
                for breach in response.json():
                    print(f"- {breach['Name']} ({breach['BreachDate']})")
            elif response.status_code == 404:
                print(f"E-Mail {email} wurde in keinem Leak gefunden.")
            else:
                print(f"Fehler: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Fehler bei der Anfrage: {e}")

    def check_file_with_virustotal(self, file_hash):
        """
        Überprüft einen Dateihash in der VirusTotal-Datenbank.
        """
        if not api.connections['virustotal']:
            print("VirusTotal-API-Key fehlt. Verbindung kann nicht hergestellt werden.")
            return

        url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
        headers = {
            'x-apikey': api.connections['virustotal']
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print(f"Ergebnisse für Datei-Hash {file_hash}:")
                for scan, details in result['data']['attributes']['last_analysis_results'].items():
                    print(f"- {scan}: {details['category']}")
            else:
                print(f"Fehler bei der Anfrage: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Fehler bei der Anfrage: {e}")
