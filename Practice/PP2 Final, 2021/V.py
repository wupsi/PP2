n, m, k = map(int, input().split())
divisor, divisors = 0, []

for i in range(1, min(n, m) + 1):
    if n % i == m % i == 0:
        divisors.append(i)
print(divisors[k - 1], divisors)