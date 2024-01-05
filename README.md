# Port Scanner

A fast and simple port scanner script written in Python. Made as a part of my Zero-To-Mastery: Ethical Hacking Bootcamp Udemy course. It allows you to scan one or multiple targets for open ports and optionally display banners.

## Prerequisites

- Python 3.x
- termcolor library (install using `pip install termcolor` or `pip3 install -r requirements.txt`)

## Usage

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using the following command:

   ```shell
   python portscanner.py [-c] [-b]
   ```

   Optional arguments:
   - `-c` or `--show-closed`: Show closed ports in the output.
   - `-b` or `--show-banners`: Show banners for open ports.

4. Enter the target(s) to scan when prompted. For multiple targets, separate them with commas.
5. Enter the port(s) to scan when prompted. For multiple ports, separate them with commas. To specify a range of ports, use a hyphen.

## Example

### Single target, single port

```shell
$ python portscanner.py
[*] Enter the target(s) to scan (for multiple tagets, separate them with ','): 192.168.1.10
[*] Enter the ports(s) to scan (for multiple ports, separate them with ','; for a range of ports use '-'): 80

[>]Checking target: 192.168.1.10
    [+] Port 80 is open.

    1 open and 0 closed ports.

    Scan on 192.168.1.10 completed in 0.01 seconds.
```

### Multiple targets, multiple ports

```shell
$ python portscanner.py
[*] Enter the target(s) to scan (for multiple tagets, separate them with ','): 192.168.1.10,192.168.1.5
[*] Enter the ports(s) to scan (for multiple ports, separate them with ','; for a range of ports use '-'): 1-100

[>]Checking target: 192.168.1.10
    [+] Port 21 is open.
    [+] Port 22 is open.
    [+] Port 23 is open.
    [+] Port 25 is open.
    [+] Port 53 is open.
    [+] Port 80 is open.

    6 open and 94 closed ports.

    Scan on 192.168.1.10 completed in 94.2 seconds.

[>]Checking target: 192.168.1.5

    All 100 scanned ports were closed.

    Scan on 192.168.1.5 completed in 0.02 seconds.
```

### Show closed ports

```shell
python3 portscanner.py -c
[*] Enter the target(s) to scan (for multiple tagets, separate them with ','): 192.168.1.5
[*] Enter the ports(s) to scan (for multiple ports, separate them with ','; for a range of ports use '-'): 1-10

[>]Checking target: 192.168.1.5
    [-] Port 1 is closed.
    [-] Port 2 is closed.
    [-] Port 3 is closed.
    [-] Port 4 is closed.
    [-] Port 5 is closed.
    [-] Port 6 is closed.
    [-] Port 7 is closed.
    [-] Port 8 is closed.
    [-] Port 9 is closed.
    [-] Port 10 is closed.  

    All 10 scanned ports were closed.

    Scan on 192.168.1.5 completed in 0.01 seconds.
```

### Show banners

```shell
python3 portscanner.py -b
[*] Enter the target(s) to scan (for multiple tagets, separate them with ','): 192.168.1.10
[*] Enter the ports(s) to scan (for multiple ports, separate them with ','; for a range of ports use '-'): 1-25

[>]Checking target: 192.168.1.10
    [+] Port 21 is open with banner 220 (vsFTPd 2.3.4).
    [+] Port 22 is open with banner SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1.
    [+] Port 25 is open with banner 220 metasploitable.localdomain ESMTP Postfix (Ubuntu).

    3 open and 22 closed ports.

    Scan on 192.168.1.10 completed in 0.17 seconds.
```

### Show closed ports and banners

```shell
python3 portscanner.py -c -b
[*] Enter the target(s) to scan (for multiple tagets, separate them with ','): 192.168.1.10
[*] Enter the ports(s) to scan (for multiple ports, separate them with ','; for a range of ports use '-'): 20-25

[>]Checking target: 192.168.1.10
    [-] Port 20 is closed.
    [+] Port 21 is open with banner 220 (vsFTPd 2.3.4).
    [+] Port 22 is open with banner SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1.
    [-] Port 23 is closed.
    [-] Port 24 is closed.
    [+] Port 25 is open with banner 220 metasploitable.localdomain ESMTP Postfix (Ubuntu).

    3 open and 3 closed ports.

    Scan on 192.168.1.10 completed in 0.05 seconds.
```
