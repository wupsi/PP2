n = int(input())
nums = list(map(int, input().split()))
main = int(input())
print(*[i * main for i in nums])