n = int(input())
nums = list(map(int, input().split()))
minx = -1e9
for i in range(len(nums)):
    if nums[i] > minx:
        minx = nums[i]
    else:
        print('Not Interesting')
        exit()
print('Interesting')