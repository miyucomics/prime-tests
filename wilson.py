while True:
    a = int(input("> "))
    result = 1
    for i in range(a - 1):
        result *= i + 1
        result %= a
    print("prime" if result == a - 1 else "composite")
