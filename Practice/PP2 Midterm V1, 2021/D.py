from collections import Counter

arr = list(map(int, input().split()))
cnt = 0
for key, value in dict(Counter(arr).most_common()).items():
    if value > 1:
        cnt += value // 2
print(cnt)