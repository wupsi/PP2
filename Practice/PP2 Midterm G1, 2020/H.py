n, h = map(int, input().split())
ans = []
for i in range(n):
    nums = list(map(int, input().split()))
    num = sum(nums) // 3
    ans.append(num)

print('YES') if max(ans) >= h else print('NO')