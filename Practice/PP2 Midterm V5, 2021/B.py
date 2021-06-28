from collections import Counter

inp = list(map(int, input().split()))

for i in Counter(inp).most_common(1):
    print(i[0])