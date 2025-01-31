from random import randint

def fermat(n, rounds):
    for i in range(rounds):
        witness = randint(2, n)
        if (witness ** (n - 1)) % n != 1:
            return False
    return True

while True:
    a, b = input("> ").split(", ")
    print(fermat(int(a), int(b)))
