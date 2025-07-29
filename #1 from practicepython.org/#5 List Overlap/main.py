import random

# lets genrate 2 randome lists

l1 = [random.randint(1, 100) for i in range(random.randint(5, 15))]
l2 = [random.randint(1, 100) for i in range(random.randint(5, 15))]


# final set with simmilar elements in bothn lists 
fl = set()


# lets find same elements in both lists

for i in l1:
    if i in l2:
        fl.add(i)

print(f"List 1:{l1}" )
print(f"List 2:{l2}" ) 
print("Final set with similar elements:", fl)        


