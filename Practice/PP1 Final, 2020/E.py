# Perfect pizza
n = int(input())
products = input().split()
ans, ingredients = [], []

for i in range(int(input())):
    ingredients.append(input().split())
main = input()

for i in range(len(ingredients)):
    if main == ingredients[i][0]:
        ans.append(ingredients[i][1])
    elif main == ingredients[i][1]:
        ans.append(ingredients[i][0])

print(len(ans))
print(*sorted(ans))