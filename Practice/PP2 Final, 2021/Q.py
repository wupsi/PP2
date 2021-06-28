n, m = map(int, input().split())

for i in range(m):
    for j in range(n):
        if i <= (m - 1) // 2 and j <= (n - 1) // 2:
            print('1', end = ' ')
        if i > (m - 1) // 2 and j > (n - 1) // 2:
            print('3', end = ' ')
        if i > (m - 1) // 2 and j <= (n - 1) // 2:
            print('2', end = ' ')
        if i <= (m - 1) // 2 and j > (n - 1) // 2:
            print('0', end = ' ')
    print()
