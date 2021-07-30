inp = list(map(int, input().split()))
for i in range(len(inp)):
    if not (65 <= inp[i] <= 90 or 97 <= inp[i] <= 122):
        print('NO')
        exit()
print('YES')