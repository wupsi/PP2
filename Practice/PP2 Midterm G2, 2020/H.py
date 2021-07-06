n = int(input())
attend = list(map(str, input().split()))
m = int(input())
group = list(map(str, input().split()))
missed, groupd = [], []

for i in attend:
    if i not in group:
        missed.append(i)
for i in group:
    if i not in attend:
        groupd.append(i)

print('Missed students:\n', end='')
for i in missed:
    print(f'- {i}')

print('Not in the group:\n', end='')
for i in groupd:
    print(f'- {i}')