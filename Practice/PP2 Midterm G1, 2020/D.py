import sys
from collections import Counter
from collections import OrderedDict

inp = list(map(str, sys.stdin.read().split()))
ans = dict(OrderedDict(sorted(dict(Counter(inp)).items(), key=lambda t: t[0])))

for key, value in ans.items():
    if value % 2 == 0:
        print(key)