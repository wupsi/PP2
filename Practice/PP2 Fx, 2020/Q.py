def sol(arr, i):
    if(i == n): return
    a.append((arr[i]) | (arr[i] + 1))
    b.append((arr[i]) & (arr[i] + 1))
    i += 1
    sol(arr, i)

a, b, cnt = [], [], 0
n = int(input())
c = list(map(int, input().split()))
sol(c, cnt)
print(*[i for i in a])
print(*[i for i in b])