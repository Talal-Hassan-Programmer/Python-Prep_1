#imports
from datetime import datetime 


name = input("Enter your name: ")
age = int(input("Enter your age: "))


current_year = datetime.now().year  
year_100 = current_year - age + 100  



print(f"Hello, {name}! You are {age} years old. You will turn 100 in the year {year_100}.")
