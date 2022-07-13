import requests
from colorama import Fore

def scanner():
    target = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target:: ")
    num_port = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter number of ports to scan:: ")
    print()

    port = 0

    for port in range(int(num_port)):
        port += 1
        url = f"http://{target}:{port}"

        try:
            requests.get(url)
        except requests.ConnectionError:
            #print(f"{Fore.RED} [!]Port {port} is close")
            pass

        else:
            print(f"{Fore.GREEN} [*]Port {port} is open")

    print(Fore.CYAN + "\n -> Scan Ended...")