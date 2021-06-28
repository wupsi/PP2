def isFibbonacci(inp):
    Fibbonacci = [0, 1, 2]
    for i in range(2, 100):
        Fibbonacci.append(Fibbonacci[i] + Fibbonacci[i - 1])

    print('YES') if inp in Fibbonacci else print('NO')

isFibbonacci(int(input()))