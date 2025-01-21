"""
    only for test purpose
"""

import paramiko

def check_ssh_conn(ip, username, password):
    """
        Versucht eine SSH-Verbindung zum Raspberry Pi herzustellen.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Um unsignierte Schlüssel zu akzeptieren

    try:
        client.connect(ip, username=username, password=password, timeout=5)
        print(f"Verbindung zu {ip} erfolgreich!")
        client.close()
        return True

    except (paramiko.AuthenticationException, paramiko.SSHException) as e:
        print(f"Fehler bei der Verbindung zu {ip}: {e}")
        return False
