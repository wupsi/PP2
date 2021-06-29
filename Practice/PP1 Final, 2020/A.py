coin1, coin2, coin3, coin4, coin5, coin6, coin7 = map(int, input().split())
coin2, coin3 = coin2 * 2, coin3 * 5
coin4, coin5 = coin4 * 10, coin5 * 20
coin6, coin7 = coin6 * 50, coin7 * 100

n, customers_list, machine_coins = int(input()), [], 0

machine_coins += coin1 + coin2 + coin3 + coin4 + coin5 + coin6 + coin7  

for i in range(n):
    customers = int(input())
    customers_list.append(customers)

for i in range(len(customers_list)):
    if machine_coins > customers_list[i]:
        print('Transaction accepted!')
        machine_coins -= customers_list[i]
    else:
        print('Transaction stopped!')