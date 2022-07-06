# Coded with <3 by C0mmand4r :)

import os
import socket
import sys
from sys import platform
import requests
from requests import post
from src import ping, whois, wordpress, host_ip, ip_info

try:
    from colorama import Fore
except:
    os.system("pip install colorama requests")
from colorama import Fore

def clear():
    if platform == 'win32':
        os.system("cls && title Web-Tool")
    if platform == 'linux' or platform == 'linux2':
        os.system("clear")
clear()

def banner():
    
    clear()
    print(f""" {Fore.CYAN}
     _       ____________     __________  ____  __
    | |     / / ____/ __ )   /_  __/ __ \/ __ \/ /
    | | /| / / __/ / __  |    / / / / / / / / / /
    | |/ |/ / /___/ /_/ /    / / / /_/ / /_/ / /___
    |__/|__/_____/_____/    /_/  \____/\____/_____/
    {Fore.RED}
            < .:: WEB-TOOLkit by C0mmand4r ::. >
    < .:: Github & Instagram & Twitter: c0mmand4r ::. >
    """)
    print(f""" {Fore.LIGHTGREEN_EX}
            [ 1 ] Ping Tool
            [ 2 ] Server whois
            [ 3 ] Admin page finder (9073 Page)
            [ 4 ] Wordpress Usernames
            [ 5 ] Host to IP
            [ 6 ] IP Information
            [ 7 ] Subdomain finder (8210 Subdomain)

            [ 99 ] EXIT

    """)

    choose = input(f"{Fore.WHITE}WEB-TOOL:~# ")


    if choose == '1':
        clear()
        ping.ping()
        input(Fore.LIGHTBLUE_EX + " [ # ] Press Enter for back to menu")
        banner()

    elif choose == '2':
        clear()
        whois.whois()
        input(Fore.LIGHTBLUE_EX + " [ # ] Press Enter for back to menu")
        banner()

    elif choose == '3':
        clear()

        try:
            website = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target:: ")
            if not website.startswith("http://") or not website.startswith("https://"):
                website  = "http://" + website

            ## url file (You can change it)
            urlfile = open("src/files/login.txt")
            print("")

            ## find admin page
            for url in urlfile:
                url = url.strip("\n")
                full_address = website + "/" + url
                response = post(full_address)
                if response.status_code == 200:
                    print(Fore.GREEN + " [ 200 ] {} ==> FOUND".format(full_address))
                else:
                    print(Fore.RED + " [ 404 ] {} ==> NOT FOUND".format(full_address))
        except:
            print(f"{Fore.RED} [ ! ] Please check your Internet connection or Domain")
        
        input(Fore.LIGHTBLUE_EX + " [ # ] Press Enter for back to menu")
        banner()

    elif choose == '4':
        clear()
        wordpress.usernames()
        print()
        input(Fore.LIGHTBLUE_EX + " [ # ] Press Enter for back to menu")
        banner()

    elif choose == '5':
        clear()
        host_ip.find()
        input(Fore.LIGHTBLUE_EX + " [ # ] Press Enter for back to menu")
        banner()

    elif choose == '6':
        clear()
        ip_info.info()
        print()
        input(Fore.LIGHTBLUE_EX + " [ # ] Press Enter for back to menu")
        banner()

    elif choose == '7':
        clear()

        target = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter yout target:: ")
        file = open("src/files/subdomain.txt")
        content = file.read()
        subs = content.splitlines()

        for subdomain in subs:
            url = f"http://{subdomain}.{target}"
            ip_url = f"{subdomain}.{target}"

            try:
                requests.get(url)

            except requests.ConnectionError:
                pass

            else:
                print(f"{Fore.GREEN} [ DISCOVERED ] {url} -> {socket.gethostbyname(ip_url)}")

        input(Fore.LIGHTBLUE_EX + " [ # ] Press Enter for back to menu")
        banner()

    elif choose == '99':
        print(Fore.RESET)
        clear()
        exit()

    else:
        print(Fore.RED + "[ ! ] Please choose a valid option")

banner()