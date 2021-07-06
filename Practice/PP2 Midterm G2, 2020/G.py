import re

txt = input()
t = input()
s = input()
f = input()

txt = re.sub(t, s, txt)
print(len(re.findall(f, txt)))