from collections import Counter

txt = list(map(str, input().split()))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
sum_words = {}

for letter in alphabet:
    sum_words[letter] = 0

for letter in alphabet:
    for i in range(len(txt)):
        words = txt[i][0].lower() + txt[i][1:]
        if words[0] == letter:
            sum_words[letter] += 1
    
for key, value in sum_words.items():
    print(value)