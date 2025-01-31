from bitarray import bitarray

limit = 100
is_composite = bitarray(limit + 1)

for number in range(2, int(limit**0.5) + 1):
    if not is_composite[number]:
        is_composite[number * number:limit + 1:number] = True

print([i for i, composite in enumerate(is_composite) if not composite])
