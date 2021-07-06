moves = input()
x, y = map(int, input().split())
posy, posx = 0, 0

for i in range(len(moves)):
    if moves[i] == 'R':
        posx += 1
    elif moves[i] == 'L':
        posx -= 1
    elif moves[i] == 'U':
        posy += 1
    elif moves[i] == 'D':
        posy -= 1
    if posx == x and posy == y:
        print('Passed')
        exit()
print('Missed')