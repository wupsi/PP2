def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
              
    return True

nums = set(map(int, input().split()))

list_nums = []
for i in nums:
    if isPowerOfTwo(i):
        list_nums.append(i)

list_nums.sort()
print(*list_nums)