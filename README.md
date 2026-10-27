# CyberSecurityProject---AttackSim
<!-- no official site warning -->
## Password Cracking Toolkit
A Python-based cybersecurity toolkit that implements dictionary and brute-force password cracking techniques to test against target hashes but to also crack hashes. The toolkit measures execution time, attempts and cracking speed to demonstrate how password length, character-set complexity and attack methodology affect password security.

## Shannon Entropy Calculator Module
Implements Shannon entropy to analyse the distribution of characters within a password and estimate its information content. 
Put simply, it quantifies, using an equation, the complexity of a password, demonstrating whether it is able to be a intractable problem(computationally practical) to a brute force scenario. 
However, it is not automatically an accurate password 'grader'. For example, a password containing repeated characters can have a lower entropy than a random password of the same length. Password predictability and common patterns also matter, like 123 or capitalised first letters also matter significantly - especially in a hybrid attack methodology.

``` bash
 >> python main.py entropy -p {PASSWORD}
``` 
It will then follow up with questioning whether you would like to search a wordlist for that password you have entered using.

# Project Overview
The Cybersecurity Toolkit is an educational Python application designed to explore password security, cryptographic hashing and password cracking techniques through practical simulations. It provides a genuine use of offline cracking of (currently exclusively) SHA-256 hashes through methods of dictionary or brute force strategies.

## Key Features
- Password Hashing: Generate SHA-256 hashes of a wordlist or individual words. Utilised in cracking modules to compare target hash against candidate hash.
- Shannon Entropy: 
