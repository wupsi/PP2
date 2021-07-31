n, m = map(int, input().split())
cabinets = list(map(int, input().split()))
free_cabinets = []

for i in range(n, m + 1):
    free_cabinets.append(i)
print(*sorted(set(free_cabinets) ^ set(cabinets)))