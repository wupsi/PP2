from collections import Counter
from collections import OrderedDict

n = int(input())
d, f, ans = {} ,{}, []
for i in range(n):
    name, gpa = input().split()
    if name not in d.keys():
        d[name] = int(gpa)
        f[name] = 1
    else:
        d[name] += int(gpa)
        f[name] += 1

d_val = list(d.values())
f_val = list(f.values())
names = list(d.keys())
for i in range(len(d_val)):
    ans.append(d_val[i] / f_val[i])
full_ans = {}
for i in range(len(d)):
    full_ans[names[i]] = ans[i]
answer = dict(OrderedDict(sorted(full_ans.items(), key=lambda t: t[0])))
for key, value in answer.items():
    print(f'{key}: {value:.3f}')