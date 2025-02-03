from math import factorial

def aks(n):
    for k in range(n):
        power = factorial(n) // (factorial(k) * factorial(n - k))
        if n - k == n:
            power -= 1
        if power % n != 0:
            return "composite"
    return "prime"

while True:
    a = input("> ")
    print(aks(int(a)))
