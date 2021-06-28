n, m = map(int, input().split())
list_num = []
sum_row, sum_list, maxi = 0, [], 0

for i in range(n):
    num = list(map(int, input().split()))
    list_num.append(num)

for i in range(n):
    for j in range(m):
        sum_row += list_num[i][j]
    sum_list.append(sum_row)
    sum_row = 0

for i in range(len(sum_list)):
    if sum_list[i] == max(sum_list):
        print(i + 1)
        break