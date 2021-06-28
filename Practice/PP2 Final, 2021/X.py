def toFixed(num):
    return f'{num:.{4}f}'

def toFix(num):
    return int(num)

n = int(input())
pairs, points = {}, 0

for i in range(n):
    Name = list((map(str, input().split())))
    points += int(Name[1])
    if Name[0] not in pairs.keys():
        pairs[Name[0]] = int(Name[1])
    else:
        pairs[Name[0]] += int(Name[1])

list_keys = list(pairs.keys())

for i in list_keys:
    pairs[i] = pairs[i] / points * 100
    if pairs[i] % int(pairs[i]) == 0:
        pairs[i] = int(toFix(pairs[i]))
    else:
        pairs[i] = float(toFixed(pairs[i]))

list_items = list(pairs.items())
list_items.sort(key = lambda i: i[1])
list_items.reverse()
for i in list_items:
    print(i[0], str(i[1]) + '%')