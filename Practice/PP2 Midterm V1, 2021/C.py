arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
n, m = map(int, input().split())
cnt = 0
try:
    for i in range(n, m):
        if arr1[i]:
            cnt += 1
        if arr2[i]:
            cnt += 1
except:
    pass
print(cnt)