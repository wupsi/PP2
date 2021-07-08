n = int(input())
d, cities = {}, []
for i in range(n):
    country = input().split()
    for i in range(2, int(country[1]) + 2):
        d[country[i]] = country[0]

m = int(input())
keys = []
for i in range(m):
    city = input()
    if city in d.keys() and d[city]:
        keys.append(d[city])
    else:
        keys.append('Unknown')

for i in keys:
    print(i)