n, m = map(int, input().split())
print(*sorted(set([i for i in range(n, m + 1)]) ^ set(list(map(int, input().split())))))