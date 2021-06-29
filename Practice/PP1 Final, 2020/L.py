import collections
from collections import Counter

n = int(input())
full_ans = []

for i in range(n):
    ans, sorted_numbers, nums = 0, {}, []
    m = int(input())
    nums = list(map(int, input().split()))
    
    numbers = dict(Counter(nums))
    numbers = collections.OrderedDict(sorted(numbers.items()))
    
    sorted_keys = sorted(numbers, key=numbers.get)
    
    for j in sorted_keys:
        sorted_numbers[j] = numbers[j]
    
    for key, value in sorted_numbers.items():
        if value == 1:
            ans = key
            break
    
    for j in range(len(nums)):
        if nums[j] == ans:
            full_ans.append(j + 1)
            break

for i in full_ans:
    print(i)