#this version is before attempting to add salting. I understand passwords would likely be salted before hashing to improve security.
#will think of way to solve this after completing attack simulation. 09.05.2026

import argparse
from Banner import display_banner, help, follow_menu_help
import sys

def main():
    if len(sys.argv) == 1:
        display_banner()
        follow_menu_help()
        return

    if sys.argv[1] == "help":
        help()
        return

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")


    # hash command
    hash_parser = subparsers.add_parser(
        "hash",
        help="Hash a wordlist"
    )

    hash_parser.add_argument(
        "-w",
        "--wordlist",
        required=True,
        help="Path to wordlist"
    )

    # entropy conmmand
    entropy_parser = subparsers.add_parser(
        "entropy",
        help = "Calculate shannon entropy on entered password"
    )

    entropy_parser.add_argument(
        "-p",
        "--password",
        required=True,
        help="Password to test stength on"
    )

    # attack command
    attack_parser = subparsers.add_parser(
        "attack",
        help = "Run attack simulation using dictionary"
    )

    attack_type = attack_parser.add_mutually_exclusive_group(required=True)

    attack_type.add_argument(
    "-d", "--dictionary",
    action="store_true",
    help="Run a dictionary attack"
    )

    attack_type.add_argument(
        "-b", "--brute-force",
        action="store_true",
        help="Run a brute-force attack"
    )

    attack_parser.add_argument(
        "-p", "--password", 
        required=True, 
        help="Target password for the simulation"
    )

    attack_parser.add_argument(
         "-w", "--wordlist", 
         required=True, 
         help="Path to the wordlist file"
     )

    

    args = parser.parse_args()
     
    if args.command == "hash":
        import Hashing
        print(f"Hashing {args.wordlist}")
        Hashing.hashing(args.wordlist)
    
    elif args.command == "entropy":
        import Entropy
        Entropy.entropy_program(args.password)

    elif args.command == "attack":
        import Attack
        if args.dictionary:
            Attack.dictionary(args.password, args.wordlist)
        elif args.brute_force:
            Attack.brute_force(args.password)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[SYSTEM] Program interrupted by user")
