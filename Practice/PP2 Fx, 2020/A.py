n = int(input())
nums = list(map(int, input().split()))
main = int(input())
cnt = 0
for i in range(len(nums)):
    if nums[i] >= main:
        cnt+= 1
print(cnt)