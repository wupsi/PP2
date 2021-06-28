import itertools

i, n = int(input()), 0

while n <= i:
    for p in itertools.product([4, 7], repeat=n):
        print(*p, end = '')
        print()
    n += 1