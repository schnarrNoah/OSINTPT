import requests
from enum import Enum
import src.utils.api_utils as api

class VirusTotalAction(Enum):
    FILE_UPLOAD = 'https://www.virustotal.com/api/v3/files'
    FILE_REPORT = 'https://www.virustotal.com/api/v3/files/{hash}'
    URL_SCAN = 'https://www.virustotal.com/api/v3/urls'

class DataHarvester:

    def __init__(self):
        """
        API init.
        """
        api.load_var()
        api.init_api_conn()

    def search_shodan(self, query):
        """
        Run shodan search.
        """
        if api.ensure_shodan_connection():
            try:
                results = api.connections['shodan'].search(query)
                for result in results['matches']:
                    print(f"IP-Adresse:\t\t{result['ip_str']}")
                    print(f"Port:\t\t\t{result['port']}")
                    print(f"Organisation:\t{result.get('org', 'N/A')}")
                    print(f"Geolocation:\t{result.get('location', 'N/A')}")
                    print(f"Service:\t\t{result.get('product', 'N/A')}")
                    print("-" * 50)
            except Exception as e:
                print(f"Error Shodan-Request: {e}")

    def check_email_pwned(self, email):
        """
        E-Mail in HIBP-Database found?.
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

    def check_with_virustotal(self, action: VirusTotalAction, value: str):
        """
        Führt eine Aktion mit der VirusTotal API aus (z. B. Datei-Upload, Bericht abrufen, URL-Scan).
        """
        if not api.connections['virustotal']:
            print("VirusTotal-API-Key fehlt. Verbindung kann nicht hergestellt werden.")
            return

        try:
            # URL und Anfrage-Parameter vorbereiten
            if action == VirusTotalAction.FILE_UPLOAD:
                url = action.value
                files = {'file': open(value, 'rb')}  # `value` ist hier der Dateipfad
                headers = {'x-apikey': api.connections['virustotal']}
                response = requests.post(url, headers=headers, files=files)
            elif action == VirusTotalAction.FILE_REPORT:
                url = action.value.format(hash=value)  # `value` ist hier der Datei-Hash
                headers = {'x-apikey': api.connections['virustotal']}
                response = requests.get(url, headers=headers)
            elif action == VirusTotalAction.URL_SCAN:
                url = action.value
                data = {'url': value}  # `value` ist hier die zu scannende URL
                headers = {'x-apikey': api.connections['virustotal']}
                response = requests.post(url, headers=headers, data=data)
            else:
                print("Ungültige Aktion.")
                return

            # Antwort prüfen und auswerten
            if response.status_code == 200:
                print(f"Erfolg: {response.json()}")
            else:
                print(f"Fehler bei der Anfrage: {response.status_code}, Antwort: {response.text}")

        except FileNotFoundError as e:
            print(f"Dateifehler: Die Datei '{value}' konnte nicht gefunden werden. Details: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Fehler bei der API-Anfrage: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")