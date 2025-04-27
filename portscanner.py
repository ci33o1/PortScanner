import socket, argparse 
import time, sys
import concurrent.futures as con
from config import *

def ARGUMENTS():
    args = argparse.ArgumentParser()
    args.add_argument('-ip', '--ip', metavar='IP', help='portscanner.py --ip <ip/domain>', type=str)
    args.add_argument('-p', '--ports', metavar='Ports Range', 
                     help="portscanner.py --ports <first-range> <second-range> (Default is All Ports)", type=int, nargs=2)
    args.add_argument('-t', '--threads', metavar='THREADS', help='portscanner.py -t <threads> (Default is 35)', type=int, default=defaultThreads)
    arguments = args.parse_args()
    ip = arguments.ip
    if not arguments.ports:
        firstRange = 0
        secondRange = 65535
    else:
        firstRange, secondRange = arguments.ports
    if ip:
        if not checkIp(arguments.ip):
            try:
                ip = socket.gethostbyname((arguments.ip))
            except socket.error:
                print(f'{dec('error', get_current_time())}Error -> Invalid Ip/hostname')
                sys.exit(1)
    return {'ip':ip,'firstRange':firstRange, 'secondRange':secondRange, 'threads':arguments.threads}


def userInput():
    try:
        targetIp = input(f"{dec('normal', get_current_time())}IP -> {WHITE}")
        if not targetIp:
            print(f'{dec('error', get_current_time())}Error -> an ip/hostname is required!{RESET}')
            sys.exit(1)
        if not checkIp(targetIp):
            try:
                targetIp = socket.gethostbyname((targetIp))
            except socket.error:
                print(f'{dec('error', get_current_time())}Error -> Invalid Ip/hostname')
                sys.exit(1)
        # Asks the user for the ports range => firstRange SecondRange
        PortsRange = input(f"{dec('normal', get_current_time())}Ports Range -> {WHITE}")
        if not PortsRange:
            firstRange = 0
            secondRange = 65535
        else:
            firstRange, secondRange = map(int, PortsRange.split())
        threads = input(f'{dec('normal', get_current_time())}Threads -> {WHITE}')
        if not threads:
            threads = defaultThreads
        
        return {"ip":targetIp, 
                "firstRange":firstRange,
                "secondRange":secondRange,
                "threads":int(threads)}
    except KeyboardInterrupt:
        sys.exit(0)

BANNER()
if len(sys.argv) > 1:
    arguments = ARGUMENTS()
else:
    arguments = userInput() 
# Threads

def scanPorts(target, firstRange, secondRange, threads):
    openPorts = 0
    start = time.time()
    def main(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            connectionResult = sock.connect_ex((target, port))
            if connectionResult == 0:
                return port
            else:
                return None 
        except socket.error as error:
            print(f'{dec('error', get_current_time())}Socket Error -> {error}')
        finally:
            sock.close()
    print(f'{dec('normal', get_current_time())}Scanning {target} on ports {firstRange}-{secondRange}.')
    with con.ThreadPoolExecutor(max_workers=threads) as exe:
        tasks = []
        for port in range(firstRange, secondRange+1):
            tasks.append(exe.submit(main, port))
        for task in con.as_completed(tasks):
            if task.result():
                openPorts += 1
                print(f'{dec('normal', get_current_time())}Open {PURPLE}[{WHITE}{portService(task.result())}{PURPLE}]-> {WHITE}{task.result()}')
    print(f'\n{dec('result', get_current_time())}Finished Scanning in {round(time.time() - start, 2)} seconds{RESET}')

scanPorts(arguments['ip'], arguments['firstRange'], arguments['secondRange'], arguments['threads'])