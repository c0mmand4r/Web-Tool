from colorama import Fore
import os

def info():
    target = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target IP:: ")
    print()
    
    ## Get Information
    os.system(f"curl https://ipinfo.io/{target}/json")