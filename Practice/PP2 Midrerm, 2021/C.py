a = list(map(int, input().split()))
b = list(map(int, input().split()))
t, cnt = int(input()), 0
for i in range(len(a)):
    if a[i] <= t <= b[i]:
        cnt += 1
print(cnt)