d, ans = dict(), []
for i in range(int(input())):
    a,b = map(int,input().split())
    try:
        ans.append(d[(min(a,b),max(a,b))])
    except:
        ans.append(0)
    d[(min(a,b),max(a,b))] = d.get((min(a,b),max(a,b)),0)+1
print('\n'.join([str(ans[i]) for i in range(len(ans))]))