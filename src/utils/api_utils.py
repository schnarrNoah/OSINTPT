'''
Funktionen:
    API-Abfragen (z. B. Shodan, Have I Been Pwned).
'''
import shodan
import requests

def search_shodan(api_key, query):
    """
        Shodan ist eine Suchmaschine für das Internet der Dinge (IoT).
        Sie kann dir helfen, Informationen über Geräte, die mit dem Internet
        verbunden sind, zu finden.
        Du kannst mit Shodan herausfinden, welche Geräte (wie Router, Server, IoT-Geräte)
        öffentlich zugänglich sind und welche Schwachstellen sie möglicherweise haben.
    """
    git add. & & git commit - m "feat: establish base code hierarchy and structure" && git push origin master

    try:
        # Suche auf Shodan mit der angegebenen Anfrage
        results = api.search(query)
        for result in results['matches']:
            print(f"IP-Adresse: {result['ip_str']}")
            print(f"Port: {result['port']}")
            print(f"Organisation: {result.get('org', 'N/A')}")
            print(f"Geolocation: {result.get('location', 'N/A')}")
            print(f"Service: {result['product']}")
            print("-" * 50)
    except shodan.APIError as e:
        print(f"Fehler bei der Shodan-Abfrage: {e}")


def check_email_pwned(email):
    """
        Have I Been Pwned ist eine Datenbank, die Informationen zu gehackten
        E-Mail-Adressen und Passwörtern enthält. Mit dieser API kannst du überprüfen,
        ob eine bestimmte E-Mail-Adresse oder ein Passwort in einem Sicherheitsvorfall
        involviert war.
    """
    url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
    headers = {'User-Agent': 'OSINT-Tool'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"E-Mail {email} wurde in den folgenden Datenschutzverletzungen gefunden:")
            breaches = response.json()
            for breach in breaches:
                print(f"- {breach['Name']} ({breach['BreachDate']})")
        elif response.status_code == 404:
            print(f"E-Mail {email} wurde in keinem Leak gefunden.")
        else:
            print(f"Fehler: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Fehler bei der Anfrage: {e}")


def check_file_with_virustotal(api_key, file_hash):
    """
        VirusTotal ist eine weitere nützliche Quelle, um Dateien und URLs auf
        Viren, Malware oder schadhafte Aktivitäten zu überprüfen.
        Die API kann verwendet werden, um die Sicherheitslage einer Domain oder einer Datei
        zu analysieren.
    """
    url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
    headers = {
        'x-apikey': api_key
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(f"Ergebnisse für Datei Hash {file_hash}:")
            for scan in result['data']['attributes']['last_analysis_results']:
                print(f"- {scan}: {result['data']['attributes']['last_analysis_results'][scan]['category']}")
        else:
            print(f"Fehler bei der Anfrage: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Fehler bei der Anfrage: {e}")
