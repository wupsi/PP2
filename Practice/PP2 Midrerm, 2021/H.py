import re 

inp = input()
nicknames, domain, suffix = [], [], []
email = re.findall(r'[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}', inp)
email.sort()
for i in email:
    nicknames.append(i.split('@')[0])
    domain.append(i.split('@')[1].split('.')[0])
    suffix.append(i.split('@')[1].split('.')[1])
print('nicknames:')
print(*nicknames)
print('domain name:')
print(*domain)
print('suffix:')
print(*suffix)