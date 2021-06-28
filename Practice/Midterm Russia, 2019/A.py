n, m = map(int, input().split())

for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:
            print('+', end = '')
        elif i == 0 and j == n - 1:
            print('+', end = '')
        elif i == m - 1 and j == 0:
            print('+', end = '')
        elif i == m - 1 and j == n - 1:
            print('+', end = '')
        elif j == 0 and i > 0 and i < m:
            print('|', end = '')
        elif j == n - 1 and i > 0 and i < m:
            print('|', end = '')
        elif i == 0 and j > 0 and j < n:
            print('-', end = '')
        elif i == m - 1 and j > 0 and j < n:
            print('-', end = '')
        else:
            print(end = ' ')
    print()