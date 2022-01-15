import socket as s
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)
from os import system
system("title " + "Programmed By Lynch - Website IP Extractor")

logo = """
  _                     _     
 | |   _   _ _ __   ___| |__  
 | |  | | | | '_ \ / __| '_ \ 
 | |__| |_| | | | | (__| | | |
 |_____\__, |_| |_|\___|_| |_|
       |___/                                    
"""

print(Fore.CYAN+logo)
title = ("Made w Love By Lynch, [i]: @l7up")
print(Fore.RED+title) 
host = input(f"[{Fore.GREEN}?{Fore.RESET}] Web To Extract IP From: ")
print(f"[{Fore.GREEN}+{Fore.RESET}] IP-Adress From {host} is [{s.gethostbyname(host)}]")
