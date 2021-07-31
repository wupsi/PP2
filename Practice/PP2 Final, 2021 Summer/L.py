from collections import Counter
cnt = 0
for key, value in dict(Counter(map(int, input().split()))).items():
    if value == 1:
        cnt += key
print(cnt)