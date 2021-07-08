import re

date = input()
if re.findall(r'\d{4} \d{2} \d{2}', date):
    if 1 <= int(re.findall(r'\d{4} \d{2} (\d{2})', date)[0]) <= 31:
        if 1 <= int(re.findall(r'\d{4} (\d{2}) \d{2}', date)[0]) <= 12:
            if 1299 <= int(re.findall(r'(\d{4}) \d{2} \d{2}', date)[0]) <= 1922:
                print('Yes')
                exit()
print('No')