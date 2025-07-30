import random

# creating 2 list randomely

a = [random.randint(1, 100) for _ in range(random.randint(1, 20))]
b = [random.randint(1, 100) for _ in range(random.randint(1, 20))]

# using set to find common elements
common_elements = list(set(a) & set(b)) # this is a way to get common elements from 2 lists in one line (i was also confused and saw something like this for first time i am also learning)

print("List A:", a)
print("List B:", b) 
print("Common elements:", common_elements)