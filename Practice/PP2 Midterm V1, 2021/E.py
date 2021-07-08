n = int(input())
d = {'a': 0, 'b': 0, 'c': 0}
for i in range(n):
    a, b, c = input().split()
    for j in a:
        if 'A' <= j <= 'Z':
            d['a'] += 1
    for j in b:
        if j.lower() == 'a' or j.lower() == 'e' or j.lower() == 'i'\
        or j.lower() == 'o' or j.lower() == 'u' or j.lower() == 'y':
            d['b'] += 1
    for j in c:
        if  '1' <= j <= '9':
            d['c'] += 1
print(d)