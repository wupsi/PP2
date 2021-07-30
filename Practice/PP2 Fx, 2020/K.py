n = int(input())
nums = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if i > 1 and i % 2 == 0 and nums[i] - nums[i - 1] >= 3: cnt += 1
print(cnt)