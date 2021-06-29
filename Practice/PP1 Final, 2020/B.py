n, k = int(input()), 0

for i in range(n * 2):
    for j in range(n * 4 - 1):
        if i == n - 1 and j > n - 1 and j < n * 4 - n - 1:
            print('*', end='')
        elif i + j == n * 2 - 1:
            print('*', end='')
        elif i == n * 2 - 1 and j != n * 2 - 1:
            print('*', end='')
        elif i + j == n * 4 - 1 and i > n - 1:
            print('*', end='')
        elif i + j == 2 * n - 1 + k:
            print('*', end='')
        elif i + j == k - 1 and i > n - 1:
            print('*', end='')
        else:
            print(end=' ')
    k += 2
    print()