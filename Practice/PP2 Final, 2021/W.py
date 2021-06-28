s = input()
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

if s == 'SUN':
    print(7)
else:
    for i in range(len(days)):
        if s == days[i]:
            print(7 - i - 1)