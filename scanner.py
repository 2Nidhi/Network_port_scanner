import socket
import threading
import argparse
import logging
from datetime import datetime

# Function to scan port and detect services
def scan_port(ip,port):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    # try to connect to thr port
    try:
        result = s.connect_ex((ip, port))
        if result==0:
            service = identify_service(port)
            logging.info(f"[+] {ip} - Port {port} is OPEN - Service: {service}")

        else:
             logging.info(f"[-] {ip} - Port {port} - CLOSED")
    except socket.error as err:
        logging.error(f"Error scanning port{ip}:{port}-{err}")
    finally:
        s.close()

# Function to identify the service based on the port
def identify_service(port):
    # simple mapping of common ports to services
    service_map={
        20: ("FTP Data", "TCP"),
        21: ("FTP Control", "TCP"),
        22: ("SSH", "TCP"),
        23: ("Telnet", "TCP"),
        25: ("SMTP", "TCP"),
        53: ("DNS", "TCP/UDP"),
        67: ("DHCP Server", "UDP"),
        68: ("DHCP Client", "UDP"),
        69: ("TFTP", "UDP"),
        80: ("HTTP", "TCP"),
        110: ("POP3", "TCP"),
        123: ("NTP", "UDP"),
        143: ("IMAP", "TCP"),
        161: ("SNMP", "UDP"),
        443: ("HTTPS", "TCP"),
        3306: ("MySQL", "TCP"),
        3389: ("RDP", "TCP"),
        
    }
    service, protocol = service_map.get(port, ("Unknown Service", "Unknown Protocol"))
    return f"{service} ({protocol})"

# Argument parser setup (CLI i/p)
def create_parser():
    parser = argparse.ArgumentParser(description="Scan ports on target IP addresses")
    # parser.add_argument("--target", type=str, required=True, help="Primary target IP address")
    parser.add_argument("--hosts", type=str, required=True, help="Comma-separated list of IPs to scan")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=65535, help="End port (default: 65535)")
    return parser

# Scans all ports for multiple hosts
def scan_multiple_hosts(target_ips, start_port, end_port):
    for ip in target_ips:
        print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
        for port in range(start_port, end_port + 1):
            t = threading.Thread(target = scan_port, args=(ip, port))
            t.start()

# Main function
def main():
    parser = create_parser()
    args = parser.parse_args()

    start_port = args.start
    end_port = args.end
    target_ips = args.hosts.split(',')

    # Setup logging
    log_filename = f"scan_results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    logging.basicConfig(filename=log_filename, level=logging.INFO)

    # Begin scanning
    scan_multiple_hosts(target_ips, start_port, end_port)

if __name__ == "__main__":
    main()