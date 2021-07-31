for i in range(int(input())):
    ans = []
    inp = input().split()
    for j in range(len(inp)):
        ans.append(len(inp[j]))
    print(*sorted(ans), 'total:', sum(ans))