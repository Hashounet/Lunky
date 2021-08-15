import socket
import sys

import pyfiglet
from rich.console import Console
from rich.table import Table

from utils import extract_json_data, threadpool_executer

console = Console()


class PScan:

    PORTS_DATA_FILE = "./common_ports.json"

    def __init__(self):
        self.ports_info = {}
        self.open_ports = []
        self.remote_host = ""

    def get_ports_info(self):
        data = extract_json_data(PScan.PORTS_DATA_FILE)
        self.ports_info = {int(k): v for (k, v) in data.items()}

    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        conn_status = sock.connect_ex((self.remote_host, port))
        if conn_status == 0:
            self.open_ports.append(port)
        sock.close()

    def show_completion_message(self, out_file):
        print()
        if self.open_ports:
            console.print("Scan terminé. Ports ouverts:", style="bold blue")
            table = Table(show_header=True, header_style="bold green")
            table.add_column("PORT", style="blue")
            table.add_column("STATE", style="blue", justify="center")
            table.add_column("SERVICE", style="blue")
            for port in self.open_ports:
                table.add_row(str(port), "OUVERT", self.ports_info[port])
            console.print(table)
            save = open(out_file, 'w')
            for port in self.open_ports:
                save.write(str(port) + " - OUVERT | " + self.ports_info[port] + "\n")
            save.close()
        else:
            console.print(f"Aucun port ouvert trouvé sur la cible", style="bold magenta")

    @staticmethod
    def show_startup_message():
        console.print(f"[bold green]Scanner de port par fchaxor[/bold green]")
        print()

    @staticmethod
    def get_host_ip_addr(target):
        try:
            ip_addr = socket.gethostbyname(target)
        except socket.gaierror as e:
            console.print(f"{e}. Exiting.", style="bold red")
            sys.exit()
        console.print(f"\nAdresse IP acquise: [bold blue]{ip_addr}[/bold blue]")
        return ip_addr

    def initialize(self, target, out_file):
        self.show_startup_message()
        self.get_ports_info()
        try:
            target = target
        except KeyboardInterrupt:
            console.print(f"\nBien reçu! Exiting.", style="bold red")
            sys.exit()
        self.remote_host = self.get_host_ip_addr(target)
        try:
            input("\nPScan est prêt. Appuyez sur entrée pour lancer le scanner.")
        except KeyboardInterrupt:
            console.print(f"\nBien reçu. Exiting.", style="bold red")
            sys.exit()
        else:
            self.run(out_file)

    def run(self, out_file):
        threadpool_executer(
            self.scan_port, self.ports_info.keys(), len(self.ports_info.keys())
        )
        self.show_completion_message(out_file)


if __name__ == "__main__":
    pscan = PScan()
    pscan.initialize(input("CIBLE: "))