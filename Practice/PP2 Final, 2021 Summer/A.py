ans = {}
for i in range(int(input())):
    name, gpa = map(str, input().split())
    if name not in ans.keys():
        ans[name] = [float(gpa)]
    else:
        ans[name].append(float(gpa))
print('\n'.join([f'{key}: {sum(value) / len(value):.3f}' for key, value in sorted(ans.items())]))