word = input()
l, r = map(int, input().split())

for i in range(len(word)):
    if l - 1 <= i < r:
        print(word[i].lower(), end = '')
    else:
        print(word[i], end = '')
