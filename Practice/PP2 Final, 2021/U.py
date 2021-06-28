h, a, b = list(map(int, input().split()))
print(int((h - a - 1) // (a - b) + 2))