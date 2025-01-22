import modules.data_harvester as dh
import utils.terminal_utils as x_tp
import utils.api_utils as x_api
import utils.file_utils as x_file


class Main:
    """
        Main entry point and program flow control
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
        x_tp.print_banner()
        match x_tp.run_ui(self.main_menu_options):
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
        print("\nStarting OSINT-Modul ...")
        match x_tp.run_ui(self.osint_menu_options):
            case 1:
                # Shodan Search
                pass
            case 2:
                # Have I Been Pwned
                pass
            case 3:
                # Virus Total Lookup
                pass
            case 4:
                # Vulnerability Lookup
                pass

    def penetration(self):
        print("\nStarting PENTESTING-Modul ...")
        match x_tp.run_ui(self.pentest_menu_options):
            case 1:
                # Brute Force with Hydra
                pass
            case 2:
                # Network Scanning with Nmap
                pass



        #print("API-Verbindungen initialisieren...")
        #x_api.init_api_conn()


        #query = "IoT devices"  # Beispiel-Query
        #self.harvester.search_shodan(query)

        #email = "example@example.com"  # Beispiel-E-Mail
        #self.harvester.check_email_pwned(email)

        #file_hash = "d41d8cd98f00b204e9800998ecf8427e"  # Beispiel-Hash
        #self.harvester.check_file_with_virustotal(file_hash)


# ============================================================================

        # Data Harvester initialisieren
        #print("Daten sammeln...")
        #self.harvester = dh.DataHarvester()

        # Beispielaufrufe von Methoden
        #self.run_harvester()



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