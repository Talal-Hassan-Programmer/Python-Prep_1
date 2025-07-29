# let do it 

#asking for a input

s = input("Enter a string: ")

# checking if the string is a palindrome
if s == s[::-1]: # s[::-1] is a reversing the string
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")