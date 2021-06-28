n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0:
            print(j, end = '')
        elif i == n - 1:
            print(n + j - 1, end = '')
        elif j == 0 and 0 < i < n - 1:
            print(i, end = '')
        elif j == n - 1 and 0 < i < n - 1:
            print(n + i - 1, end = '')
        else:
            print(end = ' ')
    print()