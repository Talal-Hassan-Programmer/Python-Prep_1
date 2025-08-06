# Pick Word

#imports
import random

# Function to pick a random word from a list
def pick_word(word_list):
    with open(word_list, 'r') as file:
        words = [line.strip().lower() for line in file if line.strip()]
    return random.choice(words)

if __name__ == "__main__":
    # Specify the path to the word list file
    word_list_path = 'C:/Users/USER/Desktop/Python Prep/Python-Prep_1/#1 from practicepython.org/#30 Pick Word/words.txt'  # Adjust the path as necessary
    # Pick a random word from the list
    random_word = pick_word(word_list_path)
    print(f"Randomly selected word: {random_word}")

