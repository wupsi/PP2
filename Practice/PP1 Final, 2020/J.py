str = input()
sub = input()

for i in range(len(str)):
    if str[-i::] + str[:-i] == sub:
        print(i)
        exit()

print('Understandable have a nice day')