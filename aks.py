from math import factorial

def aks(n):
    for k in range(1, n):
        power = factorial(n) // (factorial(k) * factorial(n - k))
        if power % n != 0:
            return "composite"
    return "prime"

while True:
    a = input("> ")
    print(aks(int(a)))
