import modules.data_harvester as dh
import utils.terminal_utils as x_tp
import utils.api_utils as x_api
import utils.file_utils as x_file
import modules.vulnerability_lookup as vuln
from dotenv import load_dotenv
import os


class Main:
    """
        Main entry point and program flow control...
    """
    main_menu_options = [
        "[1] OSINT Tools",  # osint_menu_options
        "[2] Penetration Testing Tools",  # pentest_menu_options
        "[3] View Reports"  # Navigate to file
    ]
    osint_menu_options = [
        "[1] Shodan Search",  # SHODAN
        "[2] Have I Been Pwned",  # HAVE I BEEN PWNED
        "[3] Virus Total Lookup",  # VIRUS TOTAL
        "[4] Vulnerability Lookup"  # VULNERABILITY LOOKUP
    ]
    pentest_menu_options = [
        "[1] Brute Force with Hydra",  # HYDRA
        "[2] Network Scanning with Nmap"  # NMAP
    ]

    def __init__(self):
        os.environ['TERM'] = 'xterm-256color'
        load_dotenv(dotenv_path=os.path.join(os.getcwd(), 'configurations', 'config.env'))
        x_tp.print_banner()
        match x_tp.run_case_ui(self.main_menu_options):
            case 1:
                # Call OSINT func
                self.osint()
            case 2:
                # Call PenTest func
                self.penetration()
            case 3:
                # View Reports
                x_file.open_directory_in_explorer()

#---------------------------------------------------------------------------------

    def osint(self):

        osint = dh.DataHarvester()

        print("\nStarting OSINT-Modul ...")
        match x_tp.run_case_ui(self.osint_menu_options):
            case 1:
                # Shodan Search
                x_tp.clear()
                osint.search_shodan(x_tp.run_shodan_ui())
                pass
            case 2:
                # Have I Been Pwned
                pass
            case 3:
                # Virus Total Lookup
                x_tp.clear()
                osint.check_with_virustotal(dh.VirusTotalAction.FILE_UPLOAD, x_tp.run_virustotal_ui())
                osint.check_with_virustotal(dh.VirusTotalAction.FILE_REPORT, x_tp.run_virustotal_ui())
                osint.check_with_virustotal(dh.VirusTotalAction.URL_SCAN, x_tp.run_virustotal_ui())
                pass
            case 4:
                # Vulnerability Lookup
                x_tp.clear()
                param = x_tp.run_vulnlookup_ui()
                vuln.start_metasploit_vuln_lookup(service=param['service'], version=param['version'])

                pass

    def penetration(self):
        print("\nStarting PENTESTING-Modul ...")
        match x_tp.run_case_ui(self.pentest_menu_options):
            case 1:
                # Brute Force with Hydra
                pass
            case 2:
                # Network Scanning with Nmap
                pass



# ============================================================================

    # Netzwerkinformationen abrufen
    #self.get_network_info()

    #print("Netzwerkinformationen abrufen:")

    #network_info = .get_all_network_info()

    #for info in network_info:
    #    print(f"Schnittstelle: {info['interface']}")
    #    print(f"  IP-Adresse: {info.get('ip_address', 'N/A')}")
    #    print(f"  Subnetzmaske: {info.get('subnet_mask', 'N/A')}")
    #    print(f"  Broadcast-Adresse: {info.get('broadcast_address', 'N/A')}")
    #    print(f"  MAC-Adresse: {info.get('mac_address', 'N/A')}")
    #    print(f"  Netzwerkbereich: {info.get('network_range', 'N/A')}")
    #    print()

    # print("\nHydra starten:")
    # PenTest.run_hydra()

if __name__ == "__main__":
    Main()