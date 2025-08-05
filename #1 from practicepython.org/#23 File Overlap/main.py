# File Overlap


with open('C:/Users/USER/Desktop/Python Prep/Python-Prep_1/#1 from practicepython.org/#23 File Overlap/p.txt', 'r') as file:
    f1 = file.read().splitlines()

with open('C:/Users/USER/Desktop/Python Prep/Python-Prep_1/#1 from practicepython.org/#23 File Overlap/h.txt', 'r') as file:
    f2 = file.read().splitlines()

f1 = [int(num) for num in f1]
f2 = [int(num) for num in f2]

overlap = []
for num in f1:
    if num in f2:
        overlap.append(num)


print("Numbers in both files:", overlap)