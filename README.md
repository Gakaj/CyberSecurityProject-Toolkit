# CyberSecurityProject : Password Security Toolkit Project Overview

A Python-based cybersecurity toolkit that implements dictionary and brute-force password cracking techniques to test against target hashes. The toolkit measures execution time, attempts and cracking speed to demonstrate how password length, character-set complexity and attack methodology affect password security.

The Cybersecurity Toolkit is an educational Python application designed to explore password security, cryptographic hashing and password cracking techniques through practical simulations. It provides a genuine use of offline cracking/password recovery of (currently exclusively) SHA-256 hashes through methods of dictionary or brute force strategies.
# How to install
Once in identified parent directory, for example the downloads directory, run:<br><br>
bash
```
git clone https://github.com/Gakaj/CyberSecurityProject-Toolkit.git
```
Navigate to the directory 
```
cd ..../CyberSecurityProject-Toolkit.git
```
### Base usage
Once in directory simply run:
```
python main.py
```
This will show base usage and program info. <br> For a more in depth help menu:
```
python main.py help
```

## Key Features
- Command line interfacce: Implemented command line functionality and commands using Python's **argparse**.
- Password Hashing: Generate SHA-256 hashes of a wordlist or individual words. Utilised in cracking modules to compare target hash against candidate hash.
- Entropy Analysis: Grade a password entered by a user using shannon entropy indicating an idea of its strength and resistance to password spraying and guessing attacks.
- Brute Force Attack: Generate and hash candidate passwords combinations of letters using configurable character sets and a maximum length.
- Dictionary Attack: Simulate password cracking using wordlists, hashing candidate passwords and comparing the resulting hashes against a target.
- Performance Measurement: Track the number of attempts and elapsed execution time to evaluate the efficiency of different attack methods.
# Attack module
This is the main function of the project. It allows you to perform offline SHA-256 hash cracking, but also to simulate password cracking in which it will time how long it would take to crack, attempts to reveal hash and also attempts per second. It provides dictionary and brute force functionality. 

## Dictionary Methodology
Decided with the -d tag following the attack command, then provide the arguments for the target hash or the password, then provide the wordlist to test against. <br> The program will call the hash module to convert a candidate password into a SHA-256 hash. Depending on the arguments: if you provided a plaintext password - first hash before comparing, if given a hash, do not hash again. Compare candidate hash to target hash. If do not match, increment attempts and move to next candidate.
### Usage:
```
python main.py attack -d -p {PASSWORD} -w {WORDLIST}
```
For example:
```
python main.py attack -d -p qwerty123 -w rockyou.txt
```
You may also run the -h tag at any point to view help and also the expected arguments of a command.

## Brute Force Methodology 
Decided with the -b tag following the attack command, then provide the chosen charset and maxlength of the combinations generated as well as the target. <br> The program will create a candidate using a generator function, run this candidate through the hashing module to convert to SHA-256. Then compare against provided target password or hash.<br>

You can choose a multitude of options for the charset:<br>
 | lowercase a-z | uppercase A-Z | letters a-z, A-Z | digits 0-9 | alphanumerical a-z, A-Z, 0-9 | all a-z, A-Z, 0-9, punctuation

 
 ### Usage:
 ```
python main.py attack -b --hash {SHA-256 hash} -c {CHARSET} -m {MAXLENGTH INT}
```
For example:
```
python main.py attack -b --hash 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 -c lowercase -m 5
```
```
python main.py attack -b -p world -c alphanumerical -m 5
```

# Shannon Entropy Calculator Module
Implements Shannon entropy to analyse the distribution of characters within a password and estimate its information content. 
Put simply, it quantifies, using an equation, the complexity of a password, demonstrating whether it is able to be a intractable problem(computationally practical) to a brute force scenario. 
However, it is not automatically an accurate password 'grader'. For example, a password containing repeated characters can have a lower entropy than a random password of the same length. Password predictability and common patterns also matter, like 123 or capitalised first letters also matter significantly - especially in a hybrid attack methodology.
### Usage:
```
python main.py entropy -p {PASSWORD}
``` 
It will then follow up with questioning whether you would like to search a wordlist for that password you have entered using.
<br><br>
# Hashing Module
Implemented with (currently exclusively) SHA-256. Used in the attacking module as well. It is optimised using a generator to only yield one hash at a time rather than loading the whole hashed wordlist. 
### Usage:
You can either hash an entire wordlist and output to the terminal:
```
python main.py hash -w {WORDLIST PATH}
```
Or hash just one word:
```
python main.py hash -p (WORDLIST PATH}
```
# Possible Future Improvements 
- Implementing other hash methods like MD5
- Implementing functionality to crack salted hashes like HashCat and other password recovery tools
- Implementing other cracking/attacks methodologies like mask attacks or hybrid attacks
# IMPORTANT NOTE
This is an educational program used to explore the relationship between theoretical complexity of a password and the computational resources needed to crack it.
<br>It should <ins>**not**</ins> be used to crack SHA-256 hashes or in any illegitimate way without permission outside of a safe environment out of harm. 
<br>Happy coding!





