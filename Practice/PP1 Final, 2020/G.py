import math

n, primes = int(input()), []

for num in range(2, n):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
       primes.append(num)

for i in range(2, len(primes)):
    if i in primes:
        if n - i in primes:
            print(i, n - i)
            break