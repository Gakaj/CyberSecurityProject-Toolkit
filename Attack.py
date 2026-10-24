# this is the attack module, it handles the attack logic
# it will leverage hash.py to perform the hashing of the target password and the hash of the candidate password

# the process: (dictionary attack)
# 1. Obtain target password and hash it
# 2. Open a wordlist containing candidate passwords
# 3. Read one candidate password (generator?)
# 4. Hash candidate password using hash.py 
# 5. Compare result with target hash
# 6. If they match, report success, what line it is/iteration and print it in plain text NOT HASH, report time taken as well
# 7. If they do not match, try the next candidate
# 8. If the wordlist is exhausted, report not found.

import Hashing
import time
from Banner import dictionary_banner

def read_wordlist(wordlist): # generator function to improve efficiency
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                if line.strip() != "":
                    yield line.strip()
                else:
                    file.seek(line+1)
    except OSError:
        print("[FAILURE] Failed to find path")
            


def dictionary(target, wordlist):
    

    dictionary_banner() # print banner of dictionary attack
    time.sleep(1)
    print("[INFO] Initialising dictionary attack")
    time.sleep(0.1)

    target_hash = Hashing.hash_word(target) # call hash_word function and hash target password
    print(f"[INFO] Target password hash in SHA-256: {target_hash}")
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
            print(f"[INFO] Loaded Wordlist: {wordlist}")
            
            word_count = sum(1 for line in file) # assumes one password per line, generator function to improve memory efficiency
            print(f"[INFO] Words in wordlist: {word_count}\n\n\n")
    except OSError:
        print("[FAILURE] Failed to find path")    
    attempt = 0
    found = False
    time.sleep(1)
    start_time = time.perf_counter() # start timer to see how long program elapses
    # main attack logic
    
    for candidate in read_wordlist(wordlist):
        time.sleep(0.001)
        attempt += 1 
        

        if Hashing.hash_word(candidate) == target_hash:
            found = True
            print(f"\r[ATTEMPT {attempt} / {word_count}] : {candidate} tested against target hash \x1b[K", end="", flush=True)
            print(f"\n[SUCCESS] {candidate} hash matched target")
            break
            
        print(f"\r[ATTEMPT {attempt} / {word_count}] : {candidate} tested against target hash \x1b[K", end="", flush=True)

    end_time = time.perf_counter()
    if not found:
        print("\n[FAILURE] Target not found in wordlist")

    #would you like to move to brute force on characters?
    time.sleep(1)
    print("\n[RESULTS]\n")
    time.sleep(1)
    print(f"Password revealed: {candidate}")
    print(f"Attempts: {attempt}")
    print(f"Time elapsed: {end_time - start_time:4f} seconds")

    print("\nNote the plaintext password target would not be available to be printed in actual scenario")
    print("\nThis is a educational simulation of a dictionary attack and the program would obviously not be given the plain text password.")
    print("Possibly just the hash of the target password would be supplied as the program is not attempting to enter a service")

if __name__ == "__main__":
    dictionary("hello", "C:/Users/samge/dev/ProjectsGit/Cybersecurity Project/text_files/common_passwords.txt")
