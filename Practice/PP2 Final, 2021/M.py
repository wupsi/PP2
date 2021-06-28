from collections import Counter

words = input()

cnt_words = dict(Counter(words))

list_keys = list(cnt_words.keys())
list_keys.sort()

print(len(list_keys))
for i in list_keys:
    print(i, cnt_words[i])