n = int(input())
d = {'a':0, 'b':0, 'c':0}
for i in range(n):
    abc = list(map(str, input().split()))
    for i in abc[0]:
        if 'A' <= i <= 'Z': 
            d['a'] += 1
    for i in abc[1]:
        if i in 'aeiou': 
            d['b'] += 1
    for i in abc[2]:
        if '0' <= i <= '9': 
            d['c'] += 1

print(d) 