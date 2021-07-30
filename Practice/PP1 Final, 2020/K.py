# Nurbol hacker
change, list_keys, list_values, cnt = {}, [], [], 0
for i in range(int(input())):
    nick, rename = input().split()
    change[nick] = rename

keys = list(change.keys())
values = list(change.values())

for i in range(len(keys)):
    for j in range(len(keys)):
        if keys[i] == values[j]:
            change[keys[j]] = values[i]
            cnt += 1
print()
list_items = list(change.items())
for i in range(len(list_items)):
    print(*list_items[i])

# Остается удалить последние ненужные элементы из листа