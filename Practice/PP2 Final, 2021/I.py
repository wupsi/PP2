from collections import Counter

words = list(map(str, input().split()))

cnt_words = dict(Counter(words))

list_keys = list(cnt_words.keys())
list_keys.sort()

for i in list_keys:
    print(i, cnt_words[i])