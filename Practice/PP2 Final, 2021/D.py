words, word = set(map(str, input().split())), []

for i in words:
    if i != i[::-1]:
        word.append(i)

for i in sorted(word):
    print(i)