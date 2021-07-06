n = int(input())
nums = list(map(int, input().split()))
k = int(input())
num1, num2 = '', ''

for i in range(k):
    num1 += str(nums[i])
for i in range(k, n):
    num2 += str(nums[i])
print(int(num1) * int(num2))