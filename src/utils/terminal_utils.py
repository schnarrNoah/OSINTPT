import os
import time

color = {
    'black': "\033[1;30m",
    'red': "\033[1;31m",
    'green': "\033[1;32m",
    'blue': "\033[1;34m",
    'yellow': "\033[1;33m",
    'white': "\033[1;37m",
    'purple': "\033[1;35m",
    'cyan': "\033[1;36m",
    'gray': "\033[1;37m",
    'dark_gray': "\033[0;30m",
    'light_red': "\033[0;31m",
}

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')  # Bildschirm löschen (je nach OS)

    print('\n' + color['red'] + "=" * 60)  # Grüner Balken am Anfang
    print(color['red'] + " " * 15 + "Welcome to OSINT PENETRATION")  # Titel in Blau
    print(color['red'] + "=" * 60)  # Grüner Balken am Ende

    print("\n\033[1;37m" + "Starting the Data Collection...\n")  # Start-Text in Weiß

    time.sleep(1)

    print("\033[1;33m[1] \033[1;37mSearching Shodan for IoT Devices...")  # Gelbe Nummer und weiße Beschreibung
    time.sleep(1)
    print(
        "\033[1;33m[2] \033[1;37mChecking HaveIBeenPwned for breached email...")  # Gelbe Nummer und weiße Beschreibung
    time.sleep(1)
    print(
        "\033[1;33m[3] \033[1;37mChecking VirusTotal for file hash analysis...\n")  # Gelbe Nummer und weiße Beschreibung

    print("\033[1;32m" + "=" * 60)  # Grüner Balken für das Ende


print_banner()
