# Fibonacci


def fibonacci(n):
    seq = []
    a , b = 1, 1
    for i in range(n):
        seq.append(a)
        a , b = b , a + b

    return seq


x = int(input("How many Fibonacci numbers do you want? "))

if x <= 0:
    print("Please enter a positive integer.")
else:
    f_seq = fibonacci(x)
    print(f"The first {x} Fibonacci numbers are: {f_seq}")
