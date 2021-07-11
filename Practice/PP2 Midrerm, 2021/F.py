import re

email = input()
password = input()
cnta, cntA, cnt1, cntd = 0, 0, 0, 0
if re.search(r'^(.+)#\d{4}$', email):
    if 3 <= len(email) - 5 <= 32:
        for i in range(len(password)):
            if 'a' <= password[i] <= 'z':
                cnta += 1
            if 'A' <= password[i] <= 'Z':
                cntA += 1
            if '1' <= password[i] <= '9':
                cnt1 += 1
            if password[i] == '@' or password[i] == '$' or password[i] == '@'\
            or password[i] == '&' or password[i] == '#' or password[i] == '_':
                cntd += 1
        if cnt1 >= 1 and cntA >= 1 and cnta >= 1 and cntd >= 1:
            print('Welcome to Discord')
            exit()
print('Invalid password or username')