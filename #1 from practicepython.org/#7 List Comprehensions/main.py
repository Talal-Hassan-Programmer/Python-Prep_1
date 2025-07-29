import random

# getting a randome list of numbers
a = [random.randint(1, 100) for _ in range(random.randint(5, 15))]

# makes a new list that has only the even elements of this list in it

b = [x for x in a if x % 2 == 0]

print("Original list:", a)
print("Even elements:", b)
