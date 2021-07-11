students = list(map(int, input().split()))
sID = list(map(int, input().split()))
print(list(set(students) & set(sID)))