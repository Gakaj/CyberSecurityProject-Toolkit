import os, time

def help():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r'''╔══════════════════════════════════════════════╗
║             TOOLKIT HELP MENU                ║
╚══════════════════════════════════════════════╝
CYBERSECURITY TOOLKIT - Created by an A Level Student

USAGE
  python main.py <command> [options]

COMMANDS
  hash			Hash a wordlist using sha-256
  entropy		Calculate Shannon password entropy
  attack		Run password attack simulation - main command argument
  help			Display this help menu

OPTIONS
  -h, --help		Display help of command 
  -w, --wordlist	Specify the path of a wordlist file
  -p, --password	Specify a password to analyse 


EXAMPLES
  python main.py hash -w rockyou.txt
  python main.py entropy -p qwerty123
  python main.py attack -dictionary -p qwerty123 -w rockyou.txt''')
    
def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
_________       ______                  ________           ___________ __________ 
__  ____/____  ____  /______________    ___  __/______________  /__  /____(_)_  /_
_  /    __  / / /_  __ \  _ \_  ___/    __  /  _  __ \  __ \_  /__  //_/_  /_  __/
/ /___  _  /_/ /_  /_/ /  __/  /        _  /   / /_/ / /_/ /  / _  ,<  _  / / /_  
\____/  _\__, / /_.___/\___//_/         /_/    \____/\____//_/  /_/|_| /_/  \__/  
        /____/                                                                    """)
    time.sleep(0.5)
    print("\n\n")
    print("""Please acknowledge this is an educational tool used in safe environment
taken inspiration from pentesting password cracking tools like THC Hydra.""")
    time.sleep(1.5)
    print("\nPassword security toolkit created by an A Level student")
    print("Version 1.0.0")
    time.sleep(1)
    print("---------------------------------------------------------------------")
    print("Run script again and type 'help' to view help menu")
    print(" > python main.py help")
    time.sleep(1)
    print("\nRun scripts again and type '-h' to view commands and usage")
    print(" > python main.py -h")
    time.sleep(1)
    print("\nType 'help' after command argument to see help on that feature")
    print(" > python main.py hash -h")
    print("---------------------------------------------------------------------")

    



    