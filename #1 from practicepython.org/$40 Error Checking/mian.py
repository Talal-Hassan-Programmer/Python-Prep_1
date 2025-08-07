
# Guessing Game One   

import random

def guessing_game():
    number_to_guess = random.randint(1, 9)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 9. Can you guess it?")

    while True:
        while True:
            try:
                guess = int(input("Guess a number between 1 and 9: "))
                if guess >= 1 and guess <= 9:
                    break
                else:
                    print("Your input must be a number between 1 and 9 inclusive")
            except ValueError:
                print("You must enter a number")
                


        attempts += 1
                
        if guess < number_to_guess - 3:
            print("Too low! Try again.")
        elif guess > number_to_guess + 3:
            print("Too high! Try again.")
        elif guess > number_to_guess:
            print("high but close! Try again.")
        elif guess < number_to_guess:
            print("low but close! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
        

if __name__ == "__main__":
    guessing_game() #Running the game
    print("Thank you for playing!")