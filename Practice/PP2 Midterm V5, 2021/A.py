cnt = 0
with open('test.txt') as txt:
    for line in txt:
        cnt += 1
    if cnt == 0:
        print('No')
    else: 
        print(f'Good\n{cnt}')