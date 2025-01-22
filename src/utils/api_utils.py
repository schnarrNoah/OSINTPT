import os
import shodan as s
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="../../configurations/config.env")

# API-Schlüssel laden
API_KEYS = {
    'SHODAN': os.getenv("SHODAN_API_KEY"),
    'HIBP': os.getenv("HIBP_API_KEY"),
    'VIRUSTOTAL': os.getenv("VT_API_KEY"),
}

# Globale Clients/Verbindungen
connections = {
    'shodan': None,
    'hibp': API_KEYS['HIBP'],
    'virustotal': API_KEYS['VIRUSTOTAL'],
}

def init_api_conn():
    """
    Initialisiert die Verbindungen zu den APIs und speichert sie global.
    """
    global connections
    try:
        # Shodan-Client
        if API_KEYS['SHODAN']:
            connections['shodan'] = s.Shodan(API_KEYS['SHODAN'], None)
            print("Shodan-Verbindung hergestellt.")
        else:
            print("Kein Shodan-API-Key gefunden.")

        # HIBP
        if not API_KEYS['HIBP']:
            print("Kein HIBP-API-Key gefunden.")
        else:
            print("HIBP-Verbindung hergestellt.")

        # VirusTotal
        if not API_KEYS['VIRUSTOTAL']:
            print("Kein VirusTotal-API-Key gefunden.")
        else:
            print("VirusTotal-Verbindung hergestellt.")
    except Exception as e:
        print(f"Fehler beim Initialisieren der Verbindungen: {e}")

def ensure_shodan_connection():
    """
    Stellt sicher, dass die Shodan-Verbindung existiert.
    Falls nicht, wird sie neu aufgebaut.
    """
    if not connections['shodan']:
        try:
            connections['shodan'] = s.Shodan(API_KEYS['SHODAN'])
            print("Shodan-Verbindung neu hergestellt.")
        except Exception as e:
            print(f"Fehler beim Wiederherstellen der Shodan-Verbindung: {e}")
            return False
    return True
