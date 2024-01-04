import socket
import termcolor # pip install termcolor
import time
from argparse import ArgumentParser


def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.connect((ip_address,port))
        if args.show_banners:
            banner = sock.recv(1024).decode()
            if banner:
                print('\t'+termcolor.colored(f"[+] Port {port} is open with banner {banner}.",'green'))
            else:
                print('\t'+termcolor.colored(f"[+] Port {port} is open but no banner was found.",'green'))
        else:
            print('\t'+termcolor.colored(f"[+] Port {port} is open.",'green'))

        sock.close()
        return True
    except:
        if args.show_closed:
            print('\t'+termcolor.colored(f"[-] Port {port} is closed.",'red'))
        return False

def scan_target(ip_address, ports):
    print(termcolor.colored(f"\n[>]Checking target: {ip_address}",'yellow'))
    open_count = 0
    closed_count = 0
    start_time = time.time()
    for port in ports:
        status = scan_port(ip_address, port)
        if status:
            open_count+=1
        else:
            closed_count+=1
    else:
        end_time = time.time()
        if open_count == 0:
            print('\n\t'+termcolor.colored(f"All {len(ports)} scanned ports were closed.","red"))
        else:
            print('\n\t'+termcolor.colored(f"{open_count} open and {closed_count} closed ports.","light_magenta"))
        print('\n\t'+termcolor.colored(f"Scan on {ip_address} completed in {round(end_time-start_time,2)} seconds.",'cyan'))

def scan_multiple_targets(ip_addresses,ports):
    for ip_address in ip_addresses:
        scan_target(ip_address,ports)

parser = ArgumentParser()
parser.add_argument("-c", "--show-closed", dest="show_closed", action="store_true", help="show closed ports")
parser.add_argument("-b", "--show-banners", dest="show_banners", action="store_true", help="show banners")

args = parser.parse_args()

targets = input(termcolor.colored("[*] Enter the target(s) to scan (for multiple tagets, separate them with ','): ",'light_blue'))
ports = input(termcolor.colored("[*] Enter the ports(s) to scan (for multiple ports, separate them with ','; for a range of ports use '-'): ",'light_blue'))

ip_addresses = targets.split(',')

if '-' not in ports:
    ports = list(map(int, ports.split(',')))
else:
    ran = ports.split('-')
    ports = list(range(int(ran[0]),int(ran[1])+1))

scan_multiple_targets(ip_addresses,ports)
