inp = input()
k = input()

for i in range(len(inp)):
    if inp[i] == k:
        ex = i
        break
for i in range(len(inp)):
    print(abs(ex - i), end=' ')