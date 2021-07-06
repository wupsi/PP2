from collections import Counter
from collections import OrderedDict

n, words = int(input()), []
ans = Counter()
for i in range(n):
    words.append(set(input()))

for i in range(len(words)):
    cnt = Counter(words[i])
    ans += cnt

list_keys = list(ans.keys())
list_keys.sort()
full = []
for i in list_keys:
    if ans[i] % n == 0:
        full.append(i)

if full:
    print(*full)
else:
    print("NO COMMON CHARACTERS")