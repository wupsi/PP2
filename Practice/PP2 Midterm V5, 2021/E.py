n = int(input())
Full = {}

for i in range(n):
    Name = list(map(str, input().split()))
    
    if Name[0] not in Full.keys(): 
        Full[Name[0]] = Name[1::]
    else: 
        Full[Name[0]] += Name[1::]

for key, value in Full.items():
        print(f'{key}:', *value)