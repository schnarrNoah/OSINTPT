import os
from dotenv import load_dotenv


class Main:
    def __init__(self):

        load_dotenv(dotenv_path="configurations/config.env")
        API_SHODAN = os.getenv("SHODAN_API_KEY")
        print(API_SHODAN)


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
