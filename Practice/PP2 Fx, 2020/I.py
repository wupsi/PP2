ans = [list(map(int, input().split())) for i in range(int(input()))]
for i in range(len(ans)):
    print(*[ans[i][j] for j in range(len(ans[i])) if i > j], *[1 for j in range(len(ans[i])) if i <= j])