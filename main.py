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
        "-w", "--wordlist",
        help="Path to wordlist"
    )

    hash_parser.add_argument(
        "-p", "--password",
        help = "String to hash using SHA-256"

    )

    # entropy conmmand
    entropy_parser = subparsers.add_parser(
        "entropy",
        help = "Calculate shannon entropy on entered password"
    )

    entropy_parser.add_argument(
        "-p", "--password",
        required=True,
        help="Password to test stength on"
    )

    # attack command
    attack_parser = subparsers.add_parser(
        "attack",
        help = "Run attack simulation using dictionary"
    )


    target_group = attack_parser.add_mutually_exclusive_group(required=True)

    target_group.add_argument(
        "--hash",
        dest="target_hash",
        help= "Target password hash for offline hash cracking"        
    )

    target_group.add_argument( "-p", "--password", 
        help="Plaintext password for testing" 
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

# Optional arguments attack_parser.add_argument( "-w", "--wordlist", help="Path to the wordlist file" ) 
    attack_parser.add_argument( "-m", "--max-length", 
        type=int, 
        default=4, 
        help="Maximum length of candidate passwords" 
        )

    attack_parser.add_argument(
        "-c", "--charset",
        choices=["digits", "lowercase", "uppercase", "letters", "alphanumeric", "all"],
        default="lowercase",
        help="Character set for brute force"
    )

    attack_parser.add_argument(
        "-w", "--wordlist",
        help ="Path to wordlist"
    )

    

    args = parser.parse_args()
     
    if args.command == "hash":
        import Hashing
        if args.wordlist:
            print(f"Hashing {args.wordlist}")
            Hashing.hashing(args.wordlist)
        elif args.password:
            print(f"This is the SHA-256 hash of the word {args.password}: \n{Hashing.hash_word(args.password)}")
    
    elif args.command == "entropy":
        import Entropy
        Entropy.entropy_program(args.password)

    elif args.command == "attack":
        import Attack
        import Hashing

        if args.target_hash:
            target_hash = args.target_hash
        else:
            target_hash = Hashing.hash_word(args.password)

        if args.dictionary:
            if not args.wordlist:
                attack_parser.error("Dictionary attacks require wordlist {-w/--wordlist}")
                return
            
            Attack.dictionary(target_hash, args.wordlist)

        elif args.brute_force:
            Attack.brute_force(target_hash, args.charset, args.max_length)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[SYSTEM] Program interrupted by user")
