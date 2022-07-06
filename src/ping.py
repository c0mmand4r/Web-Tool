from colorama import Fore
from sys import platform
import os

def ping():
    print(Fore.CYAN)

    ## Ping from server
    hostname = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target:: ")
    if platform == 'win32':
        response = os.system("ping " + hostname)
    if platform == 'linux' or platform == 'linux2':
        response = os.system("ping -c 1 " + hostname)
    print("")
    if response == 0:
        print (f" {Fore.WHITE}[ {Fore.RED}**{Fore.WHITE} ]", hostname, 'is up!')
    else:
        print (f" {Fore.WHITE}[ {Fore.RED}**{Fore.WHITE} ]", hostname, 'is down!')