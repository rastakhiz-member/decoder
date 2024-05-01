import base64
import webbrowser
import os
from colorama import Fore

red = Fore.RED; green = Fore.LIGHTGREEN_EX; blue = Fore.BLUE; yellow = Fore.YELLOW; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;
yellow2 = Fore.LIGHTYELLOW_EX
red2 = Fore.LIGHTRED_EX
x = 0 
os.system('cls' if os.name == 'nt' else 'clear')
while x < 1:
    print(f"""{red}
                              █████              █████      █████       ███            
                             ░░███              ░░███      ░░███       ░░░             
 ████████   ██████    █████  ███████    ██████   ░███ █████ ░███████   ████   █████████
░░███░░███ ░░░░░███  ███░░  ░░░███░    ░░░░░███  ░███░░███  ░███░░███ ░░███  ░█░░░░███ 
 ░███ ░░░   ███████ ░░█████   ░███      ███████  ░██████░   ░███ ░███  ░███  ░   ███░  
 ░███      ███░░███  ░░░░███  ░███ ███ ███░░███  ░███░░███  ░███ ░███  ░███    ███░   █
 █████    ░░████████ ██████   ░░█████ ░░████████ ████ █████ ████ █████ █████  █████████
░░░░░      ░░░░░░░░ ░░░░░░     ░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░ ░░░░░  ░░░░░░░░░ 
        {blue}created by {white}kia moghadam 
        {blue}github {white}github.com/rastakhiz-member      
        {blue}telegram {white}rastakhizTM.t.me

                            {yellow2}╔═════════════════════╗
                            {yellow2}║ {red2}[{yellow}+{red2}] {white}Tool works      {yellow2}║
                            {yellow2}║   {red2}[{yellow}1{red2}] {white}encode        {yellow2}║
                            {yellow2}║   {red2}[{yellow}2{red2}] {white}decode        {yellow2}║
                            {yellow2}║   {red2}[{yellow}3{red2}] {white}open github   {yellow2}║
                            {yellow2}║   {red2}[{yellow}4{red2}] {white}open channel  {yellow2}║
                            {yellow2}╚═════════════════════╝
          
        """)

    asd = input(Fore.RED+"\n ╔═══["+Fore.LIGHTYELLOW_EX+"root"+Fore.LIGHTGREEN_EX+"@"+Fore.LIGHTYELLOW_EX+"rastakhiz"+Fore.RED+"]"+Fore.RED+"\n ╚══\x1b[38;2;0;255;189m>>> "+Fore.MAGENTA)

    if "1" in asd:
        kok = input("")
        kok1 = base64.b64encode(kok.encode('UTF-8')).decode('ascii')
        print(f"""
    {red}---------------------------------
    {red}- {green}done {kok1}
    {red}---------------------------------
    """)
    elif "2" in asd:
        kok3 = input("kdfggh ")
        kok4 = base64.b64decode(kok3)
        kok5 = kok4.decode('UTF-8')
        print(f"""
    {red}---------------------------------
    {red}- {green}done {kok5}
    {red}---------------------------------
    """)
    if "3" in asd:
        webbrowser.open('github.com/rastakhiz-member')
    if "4" in asd:
        webbrowser.open('rastakhizTM.t.me')


#        {blue}created by {white}kia moghadam 
#        {blue}github {white}github.com/rastakhiz-member      
#        {blue}telegram {white}rastakhizTM.t.meb