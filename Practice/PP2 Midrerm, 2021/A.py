nums = list(map(str, input().split()))
cnt = 0
for i in nums:
    if len(i) % 2 == 0:
        cnt += 1
print(cnt)