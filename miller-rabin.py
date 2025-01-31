import random

def miller_rabin(n, k):
    if n <= 1:
        return "composite"
    if n <= 3:
        return "probably prime"

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return "composite"
            x = y
        if y != 1:
            return "composite"

    return "probably prime"

while True:
    a, b = input("> ").split(", ")
    print(miller_rabin(int(a), int(b)))
