import modules.data_harvester as dh
import utils.terminal_utils as x_tp
import utils.api_utils as x_api


class Main:
    def __init__(self):
        """
        Initialisiert die Anwendung, API-Verbindungen und startet den DataHarvester.
        """
        x_tp.print_banner()
        #print("API-Verbindungen initialisieren...")
        #x_api.init_api_conn()

        # Data Harvester initialisieren
        #print("Daten sammeln...")
        #self.harvester = dh.DataHarvester()

        # Beispielaufrufe von Methoden
        #self.run_harvester()

    def run_harvester(self):
        """
        Führt OSINT-Operationen durch und gibt Ergebnisse aus.
        """
        c = input("OSINT-Operationen: ")

        print("\n[1] Shodan-Suche:")
        query = "IoT devices"  # Beispiel-Query
        self.harvester.search_shodan(query)

        print("\n[2] HIBP-Überprüfung:")
        email = "example@example.com"  # Beispiel-E-Mail
        self.harvester.check_email_pwned(email)

        print("\n[3] VirusTotal-Dateiprüfung:")
        file_hash = "d41d8cd98f00b204e9800998ecf8427e"  # Beispiel-Hash
        self.harvester.check_file_with_virustotal(file_hash)





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
