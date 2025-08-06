# Pick Word

#imports
import random

# Function to pick a random word from a list
def pick_word(word_list):
    with open(word_list, 'r') as file:
        words = [line.strip().lower() for line in file if line.strip()]
    return random.choice(words)

# Specify the path to the word list file
word_list_path = 'C:/Users/USER/Desktop/Python Prep/Python-Prep_1/#1 from practicepython.org/#32 Hangman/words.txt'  # Adjust the path as necessary
# Pick a random word from the list
random_word = pick_word(word_list_path)
max_tries = 6
p = ["_"  for _ in random_word ]
print(p)
while True:
    if max_tries == 0:
        print("You lost! The word was:", random_word)
        break
    else:
        print(f"You have {max_tries} tries left.")
        


        User_input = input("Guess a letter: ").lower()
        if len(User_input) != 1 or not User_input.isalpha():
            print("Please enter a single letter.")
            continue
        if User_input in random_word:
                
            if User_input in p:
                print("You already guessed that letter.")
                continue
            # Reveal all correct letters
            for i, c in enumerate(random_word):
                if c == User_input and p[i] == "_":
                    p[i] = User_input
        else:
            print("Incorrect guess.")
            max_tries -= 1

        print(' '.join(p))

        if '_' not in p:
            print("You guessed the word!")
            break
        




