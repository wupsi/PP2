n, m = map(int, input().split())
cnt = 0
while n <= m:
    n *= 3
    m *= 2
    cnt += 1
print(cnt)