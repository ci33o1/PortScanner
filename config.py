import time, datetime, re, colorama
from colorama import Fore, Style
colorama.init()

# Colours 
PURPLE = Fore.MAGENTA + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
CYAN = Fore.CYAN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
WHITE = Fore.WHITE + Style.BRIGHT
RESET = Style.RESET_ALL

# Default threads if the user didn't enter number of threads
defaultThreads = 35
# Banner
def BANNER():
    banner = '\n\n' + fr'''{CYAN}                               /^\/^\
                             _|__|  O|
                    \/     /~     \_/ \
                     \____|__________/  \
                            \_______      \
                                    `\     \                 \
                                      |     |                  \
                                     /      /                    \
                                    /     /                       \\
                                  /      /                         \ \
                                 /     /                            \  \
                               /     /             _----_            \   \
                              /     /           _-~      ~-_         |   |
                             (      (        _-~    _--_    ~-_     _/   |
                              \      ~-____-~    _-~    ~-_    ~-_-~    /
                                ~-_           _-~          ~-_       _-~
                                   ~--______-~                ~-___-~
    - by Zakaria
    ''' + '\n\n'
    delay = 0.035
    lines = banner.split('\n')
    for line in lines:
        print(f'{CYAN}{line}')
        time.sleep(delay)
    print(RESET)

# Returns current time in this format (Hours:Minutes:Seconds)
def get_current_time():
    currentTime = datetime.datetime.now().strftime("%H:%M:%S")
    return currentTime
def portService(port):
    ports_and_services = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    135: "MSRPC",
    137: "NetBIOS",
    138: "NetBIOS",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    515: "LPD",
    587: "SMTP",
    623: "IPMI",
    631: "IPP",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    1723: "PPTP",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP Proxy"
    }

    service = ports_and_services.get(port, 'Unassigned')
    return service


def dec(type, currentTime):
    string = f"{PURPLE}[{WHITE}{currentTime}{PURPLE}] {PURPLE}[{WHITE}>{PURPLE}] | "
    errorString = f"{RED}[{WHITE}{currentTime}{RED}] {RED}[{WHITE}!{RED}] | "
    resultString = f"{BLUE}[{WHITE}{currentTime}{BLUE}] {BLUE}[{WHITE}@{BLUE}] | "
    if type == 'error':
        return errorString
    elif type == 'normal':
        return string
    elif type == 'result':
        return resultString
    return None

def checkIp(ip):
    octect = r"(2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
    ipPattern = re.compile(fr'^{octect}\.{octect}\.{octect}\.{octect}$')
    if re.match(ipPattern, ip):
        return True
    else:
        return False

