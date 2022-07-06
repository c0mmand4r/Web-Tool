from colorama import Fore
import socket

def find():
    try:
    
        ## Get IP address
        hostname = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target:: ")
        ip = socket.gethostbyname(hostname)
 
        print(f"{Fore.WHITE} [ {Fore.RED}**{Fore.WHITE} ] Hostname: " + hostname + " | " + "IP: " + ip)

    except:
        print(f"{Fore.RED} [ ! ] Error: Please check your Internet Connection or Domain")