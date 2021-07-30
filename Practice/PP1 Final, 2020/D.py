# New GPA
ans = {}
for i in range(int(input())):
    grade, credit = [], []
    given = input().split()
    Student = given[0] + ' ' + given[1]
    
    for j in range(3, len(given)):
        if j % 2 == 1:
            if given[j] == 'A+': grade.append(4.0)
            if given[j] == 'A': grade.append(3.75)
            if given[j] == 'B+': grade.append(3.5)
            if given[j] == 'B': grade.append(3.0)
            if given[j] == 'C+': grade.append(2.5)
            if given[j] == 'C': grade.append(2.0)
            if given[j] == 'D+': grade.append(1.5)
            if given[j] == 'D': grade.append(1.0)
            if given[j] == 'F': grade.append(0)
        else:
            credit.append(int(given[j]))
    
    sum_credit = 0
    for j in range(len(grade)):
        sum_credit += grade[j] * credit[j]

    ans[Student] = round(sum_credit / sum(credit), 3)

ans = sorted(sorted(ans.items()), key=lambda x:(x[1], x[0]))
for i in range(len(ans)):
    print(f'{ans[i][0]} {ans[i][1]:.3f}')