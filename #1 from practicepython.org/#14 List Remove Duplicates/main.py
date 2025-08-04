# List Remove Duplicates
#imports 
import random

#funcs

l1 = []
def gen_list():
    for i in range(random.randint(5, 15)):
        l1.append(random.randint(1, 10))


def remove_duplicates_loop():
    
    new_list = list(set(l1))  
    print("Original List:", l1)
    print("New List:", new_list)



gen_list()
remove_duplicates_loop()