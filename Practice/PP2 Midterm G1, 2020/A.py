import re

print('Found a match!') if re.findall(r'[A-Z][a-z].+', input()) else print('Not matched!')