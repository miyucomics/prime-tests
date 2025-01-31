def factorize(num):
    result = []
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            result.append(i)
            num //= i
    if num > 1:
        result.append(num)
    return result

def lucas(n):
    if n == 2:
        return True
    qs = factorize(n - 1)
    for a in range(2, n):
        if (a ** (n - 1) % n) == 1 and any(a ** ((n - 1) // q) % n != 1 for q in qs):
            return True
    return False

while True:
    print(lucas(int(input("> "))))
