#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get, ConnectionError
from colorama import Fore
from json import loads

def info():
    target = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target IP:: ")
    print()
    
    ## Get Information
    try:
        req = get(f"https://ipinfo.io/{target}/json")
        req_res = req.text
        req_res_json = loads(req)
        print(f"{Fore.WHITE}  [ {Fore.RED}*{Fore.WHITE} ] Response :")
        for key in req_res_json:
            print(f"{Fore.WHITE}   [ {Fore.RED}-{Fore.WHITE} ] {str(key)}: {str(req_res_json[key])}")
    except ConnectionError:
        print(f"\n{Fore.RED}  [!] NetWork Connection Error")
    except: ...
