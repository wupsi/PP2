n, out = int(input()), []

for i in range(n):
    a, b = map(str, input().split())
    rev1, rev2 = int(a[::-1]), int(b[::-1])
    ans = rev1 + rev2
    ans = str(ans)[::-1]
    out.append(int(ans))

for i in out:
    print(i)