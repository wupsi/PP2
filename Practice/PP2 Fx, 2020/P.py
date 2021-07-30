import math

x, y = map(int, input().split())
nums, ans = [1e9], []
for i in range(int(input())):
    u, v = map(int, input().split())
    for i in range(len(nums)):
        if math.sqrt((u - x) ** 2 + (v - y) ** 2) < nums[i]:
            nums.insert(i, math.sqrt((u - x) ** 2 + (v - y) ** 2))
            ans.insert(i, [u, v])
            break

for i in range(len(ans)):
    print(*ans[i])