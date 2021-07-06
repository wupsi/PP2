import re

print('Found a match!') if re.findall(r'^[a-zA-Z0-9_]*$', input()) else print('Not matched!')