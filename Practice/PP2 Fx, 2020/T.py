import re
ans = [input() for i in range(int(input()))]
k = int(input())
print('\n'.join([i for i in ans if int(re.findall(r'\d+', i)[0]) >= k]))