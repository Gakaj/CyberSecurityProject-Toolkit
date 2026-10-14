#this version is before attempting to add salting. I understand passwords would likely be salted before hashing to improve security.
#will think of way to solve this after completing attack simulation. 09.05.2026
import time
import Entropy
import Hashing
import argparse
from Banner import display_banner, help
import Attack
import sys

def main():
    if len(sys.argv) == 1:
        display_banner()
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

    

    args = parser.parse_args()
     
    if args.command == "hash":
        print(f"Hashing {args.wordlist}")
        Hashing.hashing(args.wordlist)
    
    elif args.command == "entropy":
        Entropy.entropy_program(args.password)

    elif args.command == "attack":
        print("Booting ")
        Attack.start()


if __name__ == '__main__':
    main()
