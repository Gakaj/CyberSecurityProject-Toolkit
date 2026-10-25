# CyberSecurityProject---AttackSim
<!-- no official site warning -->
## Password Cracking Toolkit
A Python-based cybersecurity toolkit that implements dictionary and brute-force password cracking techniques to test against target hashes. The toolkit measures execution time, attempts and cracking speed to demonstrate how password length, character-set complexity and attack methodology affect password security.

## Shannon Entropy Calculator Module
Implements Shannon entropy to analyse the distribution of characters within a password and estimate its information content. 
Put simply, it quantifies, using an equation, the complexity of a password, demonstrating whether it is able to be a intractable problem(computationally practical) to a brute force scenario. 
However, it is not automatically an accurate password 'grader'. For example, a password containing repeated characters can have a lower entropy than a random password of the same length. Password predictability and common patterns also matter, like 123 or capitalised first letters also matter significantly - especially in a hybrid attack methodology.

<details>
<summary>View Shannon Entropy Formula</summary>

Shannon entropy is calculated using:

$$
H(X)=-\sum_{i=1}^{n}p(x_i)\log_2 p(x_i)
$$

Where:
- $H(X)$ is the Shannon entropy.
- $p(x_i)$ is the probability of character $x_i$ occurring.
- $n$ is the number of distinct characters.
- $\log_2$ is the logarithm to base 2.

</details>
