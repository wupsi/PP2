ans = {}
for i in range(int(input())):
    word = input().split()
    if word[0] not in ans.keys():
        ans[word[0]] = [i[1] for i in enumerate(word) if i[0] != 0]
    else:
        ans[word[0]] += [i[1] for i in enumerate(word) if i[0] != 0]
        
for i in ans.items():
    print(str(i[0]) + ':', ', '.join([k for k in i[1]]))