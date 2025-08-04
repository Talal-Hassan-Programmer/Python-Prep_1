# Password Generator
# This program generates a random password based on user-defined criteria.

#imports 
import random
import string

special_chars = string.punctuation
letters = string.ascii_letters
digits = string.digits


def gen_pass():
    length = int(input("Enter the desired password length: "))
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_letters = input("Include letters? (y/n): ").lower() == 'y'

    fl = []
    if use_special:
        fl.append(special_chars)
    if use_digits:
        fl.append(digits)
    if use_letters:
        fl.append(letters)
            

    final_pass = []
    for i in range(length):
        if not fl:
            print("You must select at least one character type!")
            return
        
        final_pass.append(random.choice(random.choice(fl)))
    
    return ''.join(final_pass)
        



print("Welcome to the Password Generator!")

while True:
    print(gen_pass())
    