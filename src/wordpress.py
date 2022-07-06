from colorama import Fore
import os

def usernames():
    target = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target:: ")
    os.system(f"curl https://{target}/wp-json?rest_route=/wp/v2/users")
    print()