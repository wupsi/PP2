inp = input()
k = input()
ex, ans = [], []
for i in range(len(inp)):
    if inp[i] == k:
        ex.append(i)
for i in range(len(inp)):
    temp = []
    for j in range(len(ex)):
        temp.append(abs(ex[j] - i))
    ans.append(min(temp))
print(ans)