#imports
import random

l1 = [random.randint(1, 100) for i in range(random.randint(5, 15))]

def list_ends(l):
    #makes a list with the first and last digit from l1.

    l2 = []
    l2.append(l[0])
    l2.append(l[-1])

    print("The list is: " + str(l))
    #returns the new list
    return l2


print(list_ends(l1))