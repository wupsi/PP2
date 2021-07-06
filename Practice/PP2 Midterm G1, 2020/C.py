n = int(input())
nums = list(map(int, input().split()))
ans = sorted(list(set(nums)))

for i in range(len(ans)):
    print(i + 1, ans[i])