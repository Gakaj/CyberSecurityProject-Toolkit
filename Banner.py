import os, time

def help():
    pass
def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
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
    print("Run script again and type 'help' to view commands and usage")
    print(" > python main.py help")
    print("\nType 'help' after module to see help on that feature")
    print(" > python main.py hash help")
    print("---------------------------------------------------------------------")

    



    