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
from Banner import dictionary_banner, display_banner, brute_banner
import time, string

charsets = {
    "digits": string.digits,                         # 0-9
    "lowercase": string.ascii_lowercase,             # a-z
    "uppercase": string.ascii_uppercase,             # A-Z
    "letters": string.ascii_letters,                 # a-z, A-Z
    "alphanumeric": string.ascii_letters + string.digits,  # a-z, A-Z, 0-9
    "all": string.ascii_letters + string.digits + string.punctuation
    }




def read_wordlist(wordlist): # generator function to improve efficiency
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                line = line.strip()
                if line:
                    yield line
    except OSError:
        print("[FAILURE] Failed to find path")
            


def dictionary(target, wordlist):
    
    display_banner()
    dictionary_banner() # print banner of dictionary attack

    time.sleep(1)
    print("[INFO] Initialising dictionary attack")
    time.sleep(0.1)

    print(f"[INFO] Target password hash in SHA-256: {target}")
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
            print(f"[INFO] Loaded Wordlist: {wordlist}")
            
            word_count = sum(1 for line in file) # assumes one password per line, generator function to improve memory efficiency
            print(f"[INFO] Words in wordlist: {word_count}\n\n\n")
    except OSError:
        print("[FAILURE] Failed to find path")    
    attempt = 0
    found = False
    update_interval = max(1, word_count // 1000) # takes the max of the two statements - if count less than 1000, 0 would produce error.
    time.sleep(1)
    start_time = time.perf_counter() # start timer to see how long program elapses
    
    
    for candidate in read_wordlist(wordlist): # main attack logic
        
        attempt += 1 

        if Hashing.hash_word(candidate) == target:
            found = True
            end_time = time.perf_counter()
            print(f"\r[ATTEMPT {attempt} / {word_count}] : {candidate[:30]} tested against target hash \x1b[K", end="", flush=True)
            print(f"\n[SUCCESS] {candidate} hash matched target")
            time.sleep(1)
            print("\n[RESULTS]\n")
            time.sleep(1)
            print(f"Password revealed: {candidate}")
            print(f"Attempts: {attempt}")
            break
        if attempt % update_interval == 0:    
            print(f"\r[ATTEMPT {attempt} / {word_count}] : {candidate[:30]} tested against target hash \x1b[K", end="", flush=True)

    
    if not found:
        print("\n[FAILURE] Target not found in wordlist")
        end_time = time.perf_counter()
    print(f"Time elapsed: {end_time - start_time:4f} seconds")
    print(f"Attempts per second: {attempt / (end_time-start_time):4f}")


    print("\nNote the plaintext password target would not be available to be printed in actual scenario")
    print("\nThis is an educational simulation of a dictionary attack and the program would obviously not be given the plain text password.")
    print("Possibly just the hash of the target password would be supplied as the program is not attempting to enter a service")


def generate_candidates(charset, maxlength):
    import itertools
    for length in range(1, maxlength + 1):
        for combination in itertools.product(charset, repeat=length):
            yield "".join(combination)

def calculate_attempts(charset, maxlength):
    n = len(charset)
    return sum(n ** length for length in range(1, maxlength + 1)) 

def brute_force(target, charset, maxlength):
    
    display_banner()
    brute_banner()
    time.sleep(1)
    print(f"\n[INFO] Charset identified: {charset}")
    print(f"[INFO] Maxlength: {maxlength}")

    charset = charsets[charset]


    total_attempts = calculate_attempts(charset, maxlength)

    print(f"[INFO] Total attempts: {total_attempts}")
    
    time.sleep(1)
    attempt = 0
    found = False
    update_interval = max(1, total_attempts // 1000) # takes the max of the two statements - if count less than 1000, 0 would produce error.
    time.sleep(1)
    start_time = time.perf_counter()
    print("\n[INFO] Initialising brute force attack\n")

    for candidate in generate_candidates(charset, maxlength): # main attack logic
        
        attempt += 1

        if Hashing.hash_word(candidate) == target:
            end_time = time.perf_counter()
            found = True
            print(f"\r[ATTEMPT {attempt} / {total_attempts}] : {candidate} tested against target hash \x1b[K", end="", flush=True)
            print(f"\n[SUCCESS] {candidate} hash matched target")

            time.sleep(1)
            print("\n[RESULTS]\n")
            time.sleep(1)
            print(f"Password revealed: {candidate}")
            print(f"Attempts: {attempt}")
            break

        if attempt % update_interval == 0:    
            print(f"\r[ATTEMPT {attempt} / {total_attempts}] : {candidate} tested against target hash \x1b[K", end="", flush=True)
        
       
    if not found:
        end_time = time.perf_counter()
        print("\n[FAILURE] Target not discovered")
        print("[FAILURE] Target may be more characters")

    print(f"Time elapsed: {end_time - start_time:4f} seconds")
    print(f"Attempts per second: {attempt / (end_time-start_time):4f}")
    print("\nNote the plaintext password target would likely not be provided, rather the hash to recover the original password")
    print("\nThis is an educational simulation of a brute force attack and the program would obviously not be given the plain text password.")
    print("Possibly just the hash of the target password would be supplied as the program is not attempting to enter a service")



    pass



if __name__ == "__main__":
    try:
        dictionary("hello", "C:/Users/samge/dev/ProjectsGit/Cybersecurity Project/text_files/common_passwords.txt")
    except KeyboardInterrupt:
        print("[SYSTEM] Program interrupted by user")