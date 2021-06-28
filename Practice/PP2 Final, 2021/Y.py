def seven(n):
    if n == 0:
        print(0)
        exit()
    ans, cnt = [], 0
    
    while True:
        ans.append(n % 7)
        n = n // 7
        if n == 0 or n == 1:
            ans.append(n % 7)
            break
    ch = False
    
    for i in reversed(ans):
        if i != 0: 
            ch = True
        if ch: 
            print(i, end = '')

n = int(input())
seven(n)