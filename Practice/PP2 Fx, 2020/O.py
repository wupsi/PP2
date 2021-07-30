from collections import Counter
inp = dict(Counter(input()))
cnt = 0
for value in inp.values():
    if value % 2 == 1:
        cnt += 1
print('ZA WARUDO TOKI WO TOMARE') if cnt <= 1 else print('JOJO')