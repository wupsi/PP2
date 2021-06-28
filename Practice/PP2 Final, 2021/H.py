n = int(input())
pairs = {}
for i in range(n):
    Name = list((map(str, input().split())))
    
    if Name[0] not in pairs.keys():
        pairs[Name[0]] = int(Name[1])
    else:
        if int(Name[1]) > pairs[Name[0]]:   
            pairs[Name[0]] = int(Name[1])

list_keys = list(pairs.keys())
list_keys.sort()

for i in list_keys:
    print(i, pairs[i])