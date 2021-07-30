# Fence
n = int(input())
colors = list(map(int, input().split()))
maxs, index = {}, -1

for i in range(len(colors)):
    max = 0
    for j in range(index + 1, len(colors)):
        if max <= colors[j]:
            max = colors[j]
            index = j
    if max != 0:
        maxs[max] = index
print(len(maxs))