str = input()
sub = input()
index = 0

if sub in str:
    print(str)
else:
    
    for i in range(1, len(str)):
        if str[-i:] not in sub:
            break
        index = i

    print(str + sub[index:])