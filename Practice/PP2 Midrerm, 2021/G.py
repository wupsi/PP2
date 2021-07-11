n = int(input())

for i in range(n):
    lost, absent = [], []
    group = list(map(str, input().split()))
    arrived = list(map(str, input().split()))
    for j in range(len(arrived)):
        if arrived[j] not in group:
            lost.append(arrived[j])
    for j in range(len(group)):
        if group[j] not in arrived:
            absent.append(group[j])
    print('Absent:', *sorted(absent))
    print('Lost:', *sorted(lost))