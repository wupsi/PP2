import re
import itertools

s = input()
words = list(map(str, input().split()))
list_all = []
perm = list(itertools.permutations(words))

for i in range(len(perm)):
    word = ''
    for j in range(len(words)):
        word += perm[i][j]

    for pos in range(len(s)):
        if re.search(word, s[pos:]):
            list_all.append(re.search(word, s[pos:]).start() + pos)

print(set(list_all))