def isPrime(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
    return flag


nums1 = set(map(int, input().split()))
nums2 = set(map(int, input().split()))
all_nums = nums1 & nums2

for i in all_nums:
    if isPrime(i):
        print(i, end = ' ')