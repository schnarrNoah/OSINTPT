"""
Funktionen: IP-Bereichsanalyse,
            DNS-Lookup,
            Subnetzermittlung.
"""
import socket
import psutil
import ipaddress
import platform


def network_info():
    """
        :returns
            current network information and interfaces
    """
    network_info = []

    for interface_name, addrs in psutil.net_if_addrs().items():
        interface_data = {"interface": interface_name}

        for addr in addrs:
            if addr.family == socket.AF_INET:  # IPv4
                interface_data.update({
                    "ip_address": addr.address,
                    "subnet_mask": addr.netmask,
                    "broadcast_address": addr.broadcast,
                    "network_range": str(ipaddress.IPv4Network(f"{addr.address}/{addr.netmask}", strict=False))
                })

        # MAC-Address for Linux/Unix
        if platform.system() != "Windows":
            for addr in addrs:
                if addr.family == socket.AF_PACKET:
                    interface_data.update({
                        "mac_address": addr.address
                    })
        else:
            # MAC-Address for Windows
            nic_info = psutil.net_if_addrs().get(interface_name)
            if nic_info:
                for addr in nic_info:
                    if addr.family == psutil.AF_LINK:
                        interface_data.update({
                            "mac_address": addr.address
                        })

        if "ip_address" in interface_data:
            network_info.append(interface_data)

    return network_info