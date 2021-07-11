import re 

inp = input()
nicknames = re.findall(r'([a-zA-Z0-9_]+)@[a-zA-Z0-9_]+\.[a-zA-Z]{2,5}', inp)
domain = re.findall(r'[a-zA-Z0-9_]+@([a-zA-Z0-9_]+)\.[a-zA-Z]{2,5}', inp)
suffix = re.findall(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.([a-zA-Z]{2,5})', inp)
print('nicknames:')
print(*nicknames)
print('domain name:')
print(*domain)
print('suffix:')
print(*suffix)