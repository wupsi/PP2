n = int(input())
str_list = []
ans = []
full_ans = []

for i in range(n):
    str_list.append(input().split())

for i in range(len(str_list)):
    for j in range(len(str_list[i])):
        cnt = 0
        ans = []
        for k in range(len(str_list[i][j])):
            if 'a' <= str_list[i][j][k] <= 'z' or 'A' <= str_list[i][j][k] <= 'Z':
                cnt += 1
        if cnt == 2 or cnt == 4 or cnt == 8 or cnt == 16 or cnt == 32 or cnt == 64:
            ans.append('H')
        else:
            ans.append('C')
        print(*ans, end = ' ')
    print()