n = int(input())
list_nums = list(map(int, input().split()))

for i in list_nums:
    if i == max(list_nums):
        print('1', end = ' ')
    else:
        print('0', end = ' ')