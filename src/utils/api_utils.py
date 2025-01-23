import os
import shodan as s
import src.utils.terminal_utils as x_tp

API_KEYS = {}
connections = {}

def load_var():
    """
    Load keys, global clients and connections...
    """
    global API_KEYS, connections  # Only list global references that should be re-written
    API_KEYS = {
        'SHODAN': os.getenv("SHODAN_API_KEY"),
        'HIBP': os.getenv("HIBP_API_KEY"),
        'VIRUSTOTAL': os.getenv("VIRUSTOTAL_API_KEY"),
    }
    connections = {
        'shodan': None,
        'hibp': API_KEYS['HIBP'],
        'virustotal': API_KEYS['VIRUSTOTAL'],
    }

def init_api_conn():
    """
    Init API connections...
    """
    global connections
    try:
        # Shodan ----------------------------------------------------------------
        if API_KEYS['SHODAN']:
            connections['shodan'] = s.Shodan(API_KEYS['SHODAN'])  # override None-Deklaration
            print(f"{x_tp.color['green']}Shodan-Connection established.{x_tp.color['reset']}")
        else:
            print(f"{x_tp.color['red']}No Shodan-API-Key found.{x_tp.color['reset']}")
        # HIBP ------------------------------------------------------------------
        if not API_KEYS['HIBP']:
            print(f"{x_tp.color['red']}No HIBP-API-Key found.{x_tp.color['reset']}")
        else:
            print(f"{x_tp.color['green']}HIBP-Connection established.{x_tp.color['reset']}")
        # VirusTotal ------------------------------------------------------------
        if not API_KEYS['VIRUSTOTAL']:
            print(f"{x_tp.color['red']}No VirusTotal-API-Key found.{x_tp.color['reset']}")
        else:
            print(f"{x_tp.color['green']}VirusTotal-Connection established.{x_tp.color['reset']}")
    except s.APIError as e:
        print(f"{x_tp.color['red']}Shodan-API-Fehler: {e}{x_tp.color['reset']}")
    except Exception as e:
        print(f"{x_tp.color['red']}Exception error: {e}{x_tp.color['reset']}")


def ensure_shodan_connection():
    """
    Shodan API established?...
    """
    global connections
    if not connections['shodan']:
        try:
            connections['shodan'] = s.Shodan(API_KEYS['SHODAN'])
        except Exception as e:
            print(f"{x_tp.color['red']}Error to reconnect Shodan: {e}{x_tp.color['reset']}")
            return False
    return True
