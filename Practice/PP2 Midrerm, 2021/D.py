ans = []
for i in range(int(input())):
    cnt = 0
    inp = input()
    words = inp.split()
    if len(inp) % 2 == 0:
        if 'A' <= inp[0] <= 'Z':
            if inp[-1] == '3' and inp[-2] == '3':
                print('yes')
                for i in range(len(words)):
                    if (len(inp[i]) % 2 != 0 and i % 2 == 0) or (i % 2 != 0 and len(inp[i]) % 2 == 0):
                        cnt += 1
    if cnt != len(words): ans.append('Seriously?')
    else: ans.append('Wow! That is perfect')
print('\n'.join([x for x in ans]))