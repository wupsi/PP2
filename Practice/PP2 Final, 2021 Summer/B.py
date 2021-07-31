from collections import Counter
print('\n'.join([f'{key} - {value}' for key, value in sorted(dict(Counter(input().split())).items())]))