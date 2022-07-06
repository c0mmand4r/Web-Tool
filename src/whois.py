from colorama import Fore
import socket

def whois():
    dm = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target:: ").lower()
    domain = dm.replace("http://", "")
    domain = dm.replace("https://", "")
    domain = dm.replace("www.", "")
    if domain[-3:] == "org" or domain[-3:] == "com" or domain [-3:] == "net":
        srv = "whois.internic.net"
    else:
        srv = "whois.iana.org"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((srv, 43))
    s.send((dm+"\r\n").encode())
    rs = s.recv(10000).decode()
    print(rs)