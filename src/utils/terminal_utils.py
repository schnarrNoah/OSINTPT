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
    'reset': "\033[0m"
}

def print_banner():
    """
    Shows banner
    """
    clear()
    print('\n' + color['red'] + "=" * 60)
    print(color['red'] + " " * 15 + "Welcome to OSINT PENETRATION")
    print(color['red'] + "=" * 60 + color['reset'])

def run_case_ui(menu_options):
    """
    Run user interface and catches input dynamically
    """
    for option in menu_options:
        time.sleep(0.25)
        print(color['yellow'] + option[:len(menu_options)] + color['white'] + option[len(menu_options):])
    time.sleep(0.25)
    print(f"{color['green']}=" * 60 + f"{color['reset']}\n")

    # User selection
    while True:
        try:
            case = int(input("\t> "))
            if 1 <= case <= len(menu_options):
                return case
            else:
                print(f"{color['red']} Bitte wähle eine gültige Option (1-{len(menu_options)})." + color['reset'])
        except ValueError:
            print(color['red'] + "Ungültige Eingabe. Bitte eine Zahl eingeben." + color['reset'])


def run_shodan_ui():
    return input(f"{color['blue']}\tSearch shodan > {color['red']}")

def run_virustotal_ui():
    return input(f"{color['blue']}\tSearch virustotal > {color['red']}")

def run_vulnlookup_ui():
    param = {
        'service' : input(f"{color['blue']}\tSearch for service > {color['red']}"),
        'version' : input(f"{color['blue']}\tVersion of service > {color['red']}"),
    }
    return param

##############################################################################################

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # Bildschirm löschen (je nach OS)

def loading_animation():
    for char in "==" * 30:
        print(color['red'] + char, end="", flush=True)
        time.sleep(0.1)
    print(color['reset'])  # Farbe zurücksetzen