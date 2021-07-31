from collections import Counter
for key, value in sorted(dict(Counter(input().split())).items()):
    print(f'{key} - {value}')