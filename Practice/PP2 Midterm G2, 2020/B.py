import re

inp = input()
search = input()
x = re.search(search, inp)
print(f'First time {search} occured in position: {x.start()}') if x else print('Not found')