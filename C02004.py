n = int(input())
for i in range(1,n + 1):
    for j in range(1,2*n):
        if i == 1:
            if j <= n - i : print('~',end='')
            else: print('*',end='')
        elif i == n  :
            if j <= n :print('*',end='')
        else:
            if j <= n - i  : print('~',end='')
            elif j == n - i + 1 or j == 2*n - i :print('*',end='')
            elif j <= 2*n - i - 1:print('.',end='')
    print('')
