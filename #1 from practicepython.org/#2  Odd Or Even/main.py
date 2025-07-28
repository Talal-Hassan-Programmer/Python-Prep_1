# This code checks if a number is odd or even based on user input.
# It uses the modulus operator to determine the remainder when the number is divided by 2.


num = int(input("Enter a number: "))

c = num % 2

if c > 0:
    print("The number is odd.")
else:
    print("The number is even.")    



