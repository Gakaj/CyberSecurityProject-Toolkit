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

def dictionary(target, wordlist):
    
    target_hash = Hashing.hash_word(target)
    print(target_hash)