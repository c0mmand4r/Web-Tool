#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import Fore
import os

def ping():
    print(Fore.CYAN)

    ## Ping from server
    hostname = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target:: ")
    
    # posix, nt =~ unix, win32
    response = os.system(f"ping{' -c 1' if os.name == 'posix' else ''} {hostname}")
        
    print (f"\n {Fore.WHITE}[ {Fore.RED}**{Fore.WHITE} ] {hostname} is {'up' if response == 0 else 'down'}!")
