def isPrime(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
    return flag

n, m = map(int, input().split())
Prime_list = []

for i in range(n, m):
    if not isPrime(i) and i != 1:
        Prime_list.append(i)

Prime_list.reverse()
print(*Prime_list)