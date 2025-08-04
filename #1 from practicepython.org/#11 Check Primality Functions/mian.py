

def devisors(num):
    f = []
    for i in range(1, num + 1):
        if num % i == 0:
            f.append(i)

    if len(f) == 2:
        return "It is a prime number"    
    else:
        return "It is not a prime number, its divisors are: " + str(f)

print(devisors(int(input("Enter a number: "))))
