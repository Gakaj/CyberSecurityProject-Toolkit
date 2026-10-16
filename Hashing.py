import hashlib


# -- >  """" Sha 256 program starts here """
def read_hash_wordlist(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
      for line in file:
        original = line.strip() # remove whitepsace and other problems
        
        if not original: # skip if empty/errors to continue
          continue #go to next iteration


        hashed = hashlib.sha256(original.encode()).hexdigest() # encode data and transform into sha256 hash
        # as well as making it a hex NOT a byte and not output object.
        yield hashed # makes the function a generator by returning an iterable - makes it more efficient as no longer held in RAM

def hashing(wordlist):
  for line in read_hash_wordlist(wordlist): #print every hashed line
    print(line)

def hash_word(target):
  return hashlib.sha256(target.encode()).hexdigest()

if __name__ == "__main__":
  hashing()
else:
  pass