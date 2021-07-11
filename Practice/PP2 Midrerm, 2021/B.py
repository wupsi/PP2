nums = list(map(int, input().split()))
k = int(input())
ans = []
for i in range(1, max(nums)):
    if i not in nums:
        ans.append(i)
print(ans[k - 1])