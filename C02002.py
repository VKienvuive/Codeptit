n = int(input())
for i in range(1,n + 1):
    for j in range(1,2*n):
        if j <= n - i : print('~',end='')
        elif j <= 2*n - i  :print('*',end='')
    print('')
