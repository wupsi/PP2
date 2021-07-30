from collections import Counter
n = int(input())
letters = dict(Counter(''.join([''.join([i for i in dict(Counter(input())).keys()]) for x in range(n)])))
ans = [key for key, value in letters.items() if value == n]
print(' '.join(i for i in ans)) if len(ans) > 0 else print('NO COMMON CHARACTERS')