n, cnt = int(input()), 0
change, list_keys, list_values = {}, [], []

for i in range(n):
    nick, rename = input().split()
    change[nick] = rename

keys = list(change.keys())
values = list(change.values())

for i in range(len(keys)):
    for j in range(len(keys)):
        if keys[i] == values[j]:
            change[keys[j]] = values[i]
            cnt += 1

list_items = list(change.items())
for i in range(len(list_items)):
    print(*list_items[i])

# Остается удалить последние ненужные элементы из листа