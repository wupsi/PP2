nums = list(map(int, input().split()))
b = nums.copy()
b.sort()
cnt = 0
for i in range(len(nums)):
    if nums[i] != b[i]:
        cnt += 1
print(cnt)
