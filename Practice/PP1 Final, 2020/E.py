n = int(input())
useless = list(map(str, input().split()))
m = int(input())
pair, ingredients = [], []

for i in range(m):
    item1, item2 = map(str, input().split())
    pair.append(item1)
    pair.append(item2)

main = input()

for i in range(len(pair)):
    if i % 2 == 0 and main == pair[i]:
        ingredients.append(pair[i + 1])
    elif i % 2 == 1 and main == pair[i]:
        ingredients.append(pair[i - 1])

print(*sorted(ingredients))