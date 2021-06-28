n, leaves1, leaves2, diff = int(input()), [], [], []

leaves1 = list(map(int, input().split()))
leaves2 = list(map(int, input().split()))

for i in range(n):
    diff.append(leaves1[i] - leaves2[i])

print(max(diff))