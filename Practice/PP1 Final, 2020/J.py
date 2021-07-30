# Understandable have a nice day
s = input()
sub = input()
for i in range(len(s)):
    if s[-i::] + s[:-i] == sub:
        print(i)
        exit()
print('Understandable have a nice day')