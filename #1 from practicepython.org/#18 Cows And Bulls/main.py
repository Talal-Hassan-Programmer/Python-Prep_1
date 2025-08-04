# Cows And Bulls

#imports
import random

# Function to generate a random 4-digit number
def generate_number():
    return str(random.randint(1000, 9999))    




#Game 
number = generate_number()
attempts = 0

print("Welcome to Cows and Bulls!")
print("Try to guess the 4-digit number. Type 'exit' to quit.")

while True:
    guess = input("Enter your guess: ")

    if guess.lower() == 'exit':
        print("Thanks for playing!")
        break

    if len(guess) != 4 or not guess.isdigit():
        print("Please enter a valid 4-digit number.")

    else:

        attempts += 1
        if guess == number:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break
        else:
            cows = 0
        bulls = 0
        number_checked = []
        guess_checked = []

        # First pass: check for cows (correct digit in correct place)
        for i in range(4):
            if guess[i] == number[i]:
                cows += 1
                number_checked.append(i)
                guess_checked.append(i)

        # Second pass: check for bulls (correct digit, wrong place)
        for i in range(4):
            if i in guess_checked:
                continue  # already matched as a cow
            for j in range(4):
                if j in number_checked:
                    continue  # already matched
                if guess[i] == number[j]:
                    bulls += 1
                    number_checked.append(j)
                    break  # stop after first match

        print(f"{cows} Cows, {bulls} Bulls. Try again!")