steps = int(input())
alp, ans = input(), ''
for i in range(len(alp)):
    if 65 <= ord(alp[i]) + steps <= 90: 
        ans += chr(ord(alp[i]) + steps)
    else:
        ans += chr((ord(alp[i]) + steps) % 90 + 64)
print(ans)