import re

date = input()
if 1 <= int(re.findall(r'(\d+)\.\d+.\d+', date)[0]) <= 31:
    if 1 <= int(re.findall(r'\d+\.(\d+)\.\d+', date)[0]) <= 12:
        if 1299 <= int(re.findall(r'\d+\.\d+\.(\d+)', date)[0]) <= 1922:
            print('YES')
            exit()
print('NO')