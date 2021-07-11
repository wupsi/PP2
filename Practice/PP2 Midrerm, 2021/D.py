def check(inp):
    if len(inp) % 2 == 0:
        if 'A' <= inp[0] <= 'Z':
            if inp[-1] == '3' and inp[-2] == '3':
                words = inp.split()
                for i in range(len(words)):
                    if len(words[i]) % 2 == 0 and i % 2 == 0:
                        print('Wow! That is perfect.')
                        exit()
n = int(input())

for i in range(n):
    inp = input()
    check(inp)
print('Seriously?')