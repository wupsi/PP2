with open('input.txt') as txt:
    temp = ''
    for line in txt:
        if len(line) < len(temp):
            print('NO')
            exit()
        temp = line
    print('YES')