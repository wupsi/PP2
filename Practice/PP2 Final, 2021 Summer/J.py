import re

txt = input()
txt = txt.upper()
x = re.search("^PP2.*MIDTERM$", txt)
if x:
    print("Success")
else:
    print("No")