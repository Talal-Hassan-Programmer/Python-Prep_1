# This script finds the factors of a given number.
# It prompts the user to input a number and then calculates its factors.

num = int(input("Enter a number: "))
f = []
for i in range(1, num + 1):
   if num % i == 0:
       f.append(i)

print(f"Factors of {num} are: {f}")

