n, m = map(int, input().split())
daddylist, sonlist, ans = [], [], {}
for i in range(m):
    daddy, son = map(int, input().split())
    daddylist.append(daddy)
    sonlist.append(son)
    ans[daddy] = 0

for i in range(len(sonlist)):

    if sonlist[i] in daddylist and sonlist[i] in ans.keys():
        ans[sonlist[i]] += 1
print(ans)