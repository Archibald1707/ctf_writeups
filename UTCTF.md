# UTCTF
It was not possible to solve the tasks for a long time, so there are very few solutions ;(

## Contract
This challenge contained pdf file, so i just used webtool to exif info from it) [Link to pdf file](https://github.com/Archibald1707/ctf_writeups/blob/master/img/additional_content/contract.pdf)

![contract](https://github.com/Archibald1707/ctf_writeups/blob/master/img/contract.png)

flag: `utflag{s1mpl3_w1z4rding_mist4k3}`

## RSA-256

```
N = 77483692467084448965814418730866278616923517800664484047176015901835675610073
e = 65537
c = 43711206624343807006656378470987868686365943634542525258065694164173101323321
```

I mean, should i explain myself at this point?

flag: `utflag{just_send_plaintext}`

## numbers go brr
This challenge was available by `nc betta.utctf.live 7356`

It provided us with a choice of 2 functions:
1. get the encrypted flag
2. encrypt any message

Here's the backend code:
###### **`python`**
```python
#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import random

seed = random.randint(0, 10 ** 6)
def get_random_number():
    global seed 
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed

def encrypt(message):
    key = b''
    for i in range(8):
        key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext.hex()

print("Thanks for using our encryption service! To get the encrypted flag, type 1. To encrypt a message, type 2.")
while True:
    print("What would you like to do (1 - get encrypted flag, 2 - encrypt a message)?")
    user_input = int(input())
    if(user_input == 1):
        break

    print("What is your message?")
    message = input()
    print("Here is your encrypted message:", encrypt(message.encode()))


flag = open('/src/flag.txt', 'r').read();
print("Here is the encrypted flag:", encrypt(flag.encode()))
```

It seemed to use AES-128 encryption in the ECB mode, but the main vulnerability was that if we discovered the original key, we would be able to decrypt all subsequent encrypted messages. And the key, in turn, could be no more than 10^6, so i naturaly wrote scrypt to bruteforce it:
###### **`python`**
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import random

def get_random_number(seed):
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed

def decrypt(ciphertext_hex, initial_seed):
    ciphertext = bytes.fromhex(ciphertext_hex)
    key = b''
    for i in range(8):
        key += (get_random_number(initial_seed) % (2 ** 16)).to_bytes(2, 'big')
        initial_seed = get_random_number(initial_seed)  # update seed for next iteration
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext.decode()
    except ValueError:
        # Decryption failed (possibly due to incorrect key), return None
        return None

def brute_force_decrypt(encrypted_flag_hex):
    for initial_seed in range(10**6 + 1):
        decrypted_flag = decrypt(encrypted_flag_hex, initial_seed)
        if decrypted_flag is not None:
            print("Decrypted flag:", decrypted_flag)
            return True  # Flag decrypted successfully
    print("Failed to decrypt flag.")
    return False  # Flag decryption failed

# Example usage:
encrypted_flag_hex = input("Enter the encrypted flag in hexadecimal: ")
brute_force_decrypt(encrypted_flag_hex)
```
And got the flag: `utflag{deep_seated_and_recurring_self-doubts}`

## Cryptordle
This challenge was available by `nc betta.utctf.live 7496`

It thought of a word, and we had to guess it in 6 guesses. And repeat it three times.

Here's the backend code:
###### **`python`**
```python
#!/usr/bin/env python3
import random

wordlist = open('/src/wordlist.txt', 'r').read().split('\n')

for word in wordlist:
    assert len(word) == 5
    for letter in word:
        assert letter in 'abcdefghijklmnopqrstuvwxyz'

for attempt in range(3):
    answer = random.choice(wordlist)
    num_guesses = 0
    while True:
        num_guesses += 1

        print("What's your guess?")
        guess = input().lower()

        assert len(guess) == 5
        for letter in guess:
            assert letter in 'abcdefghijklmnopqrstuvwxyz'

        if guess == answer:
            break

        response = 1
        for x in range(5):
            a = ord(guess[x]) - ord('a')
            b = ord(answer[x]) - ord('a')
            response = (response * (a-b)) % 31
        print(response)
    if num_guesses > 6:
        print("Sorry, you took more than 6 tries. No flag for you :(")
        exit()
    else:
        print("Good job! Onward...")

if num_guesses <= 6:
    print('Nice! You got it :) Have a flag:')
    flag = open('/src/flag.txt', 'r').read()
    print(flag)
else:
    print("Sorry, you took more than 6 tries. No flag for you :(")
```

So after you guess anything, it basically take difference modulus of `ord` 1st letter in your guess and answer, multiply it on the response variable (that equals 1 at the start), take remainder of division by 31, put that in response variable, and then proceeds to do it for every letter (5 times total), as if that response will help you solve this challenge >:(

This challenge took years from me, because no matter what script i wrote to solve it, i always was ending up without any possible choices. And after millions of tries on fixing code, i thought that problem might actually be in the wordlist. So, the only natural solution that i found, was just to simply create program that based on your guess and response from the chal filters out improper 5 letter combinations:

###### **`python`**
```python
import itertools

def calculate_response(guess, answer):
    response = 1
    for x in range(5):
        a = ord(guess[x]) - ord('a')
        b = ord(answer[x]) - ord('a')
        response = (response * (a-b)) % 31
    return response

#wordlist = open('sgb-words.txt', 'r').read().split('\n')

def generate_wordlist():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    wordlist = [''.join(w) for w in itertools.product(alphabet, repeat=5)]
    return wordlist

def filter_words(possible_words, last_guess, last_response):
    filtered_words = []
    for word in possible_words:
        if calculate_response(last_guess, word) == last_response:
            filtered_words.append(word)
    return filtered_words

def main():
    possible_words = generate_wordlist()
    guesses = []
    responses = []

    for _ in range(6):  # Assuming the original program allows 3 attempts
        last_guess = input("Last guess: ").lower()
        last_response = int(input("Last response: "))
        guesses.append(last_guess)
        responses.append(last_response)

        if last_guess:
            possible_words = filter_words(possible_words, last_guess, last_response)
        else:
            print("Invalid guess. Please provide a valid guess.")

        print("Possible words remaining:", possible_words)

        if len(possible_words) == 1:
            print("The word is:", possible_words[0])
            break

if __name__ == "__main__":
    main()

```

And that was basically it. flag: `utflag{sometimes_pure_guessing_is_the_strat}`

All the python code you can find in [misc folder](https://github.com/Archibald1707/ctf_writeups/tree/master/misc)