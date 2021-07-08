n = int(input())
for i in range(n):
    cnt_a, cnt_b, cnt_c = 0, 0, 0
    a, b, c = input().split()
    for j in a:
        if 'a' <= j.lower() <= 'z':
            cnt_a += 1
    for j in b:
        if j.lower() == 'a' or j.lower() == 'e' or j.lower() == 'i'\
        or j.lower() == 'o' or j.lower() == 'u' or j.lower() == 'y':
            cnt_b += 1
    for j in c:
        if  '1' <= j <= '9':
            cnt_c += 1
    print(cnt_a, cnt_b, cnt_c)