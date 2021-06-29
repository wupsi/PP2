n, k = int(input()), 0
student, student_name = {}, ''
gpa_grade, gpa_credits, grading = [], [], []


for i in range(n):
    inp = list(map(str, input().split()))
    student_name = inp[0] + ' ' + inp[1]
    number_subjects = int(inp[2])
    grading.append(inp[3:])
    student[student_name] = number_subjects


for i in range(len(grading)):
    grading.append(0)
    for j in range(len(grading[i])):
        if j % 2 == 0:
            if grading[i][j] == 'A+':
                gpa_grade.append(4)
            if grading[i][j] == 'A':
                gpa_grade.append(3.75)
            if grading[i][j] == 'B+':
                gpa_grade.append(3.5)
            if grading[i][j] == 'B':
                gpa_grade.append(3)
            if grading[i][j] == 'C+':
                gpa_grade.append(2.5)
            if grading[i][j] == 'C':
                gpa_grade.append(2)
            if grading[i][j] == 'D+':
                gpa_grade.append(1.5)
            if grading[i][j] == 'D':
                gpa_grade.append(1)
            if grading[i][j] == 'F':
                gpa_grade.append(0)
        else:
            gpa_credits.append(int(grading[i][j]))


for key, value in student.items():
    sum_gpa_credits = 0
    top = 0
    for i in range(k, k + value):
        top += gpa_credits[i] * gpa_grade[i]
        sum_gpa_credits += gpa_credits[i]
        k += 1
    student[key] = top / sum_gpa_credits


list_gpa = list(student.items())
list_gpa.sort(key = lambda i: i[1])

for i in list_gpa:
    print(i[0], round(i[1], 3))