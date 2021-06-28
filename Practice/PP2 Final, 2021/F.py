def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
              
    return True

nums = set(map(int, input().split()))

for i in nums:
    if not isPowerOfTwo(i):
        print(i, end = ' ')