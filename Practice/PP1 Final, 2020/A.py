# Transaction
coin1, coin2, coin3, coin4, coin5, coin6, coin7 = map(int, input().split())
coin2, coin3, coin4 = coin2 * 2, coin3 * 5, coin4 * 10
coin5, coin6, coin7 = coin5 * 20, coin6 * 50, coin7 * 100
money = coin1 + coin2 + coin3 + coin4 + coin5 + coin6 + coin7
ans = []

for i in range(int(input())):
    customer = int(input())
    if money >= customer:
        ans.append('Transaction accepted!')
        money -= customer
    else: ans.append('Transaction stopped!')

for i in range(len(ans)):
    print(ans[i])