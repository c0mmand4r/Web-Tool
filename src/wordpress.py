#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get, ConnectionError
from colorama import Fore, Back , Style

def usernames():
    target = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target:: ")
    try:
        req = get(f"https://{target}/wp-json?rest_route=/wp/v2/users")
        req_res = req.text
        print(f'''
{Fore.WHITE}  [ {Fore.RED}*{Fore.WHITE} ] Response : {Fore.LIGHTWHITE_EX}

{Back.WHITE}{req_res}{Style.RESET_ALL}

{Fore.RESET}''')
    except ConnectionError:
        print(f"\n{Fore.RED}  [!] NetWork Connection Error")
    except: ...
    print()