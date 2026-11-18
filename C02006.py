a , b = map(int,input().split())
for i in range(a):
    for j in range(b + i):
        if i == 0  : print('*',end='')
        elif i == a - 1:
            if j < i : print('~',end='')
            else : print('*',end='')
        elif j < i : print('~',end='')
        elif j == i or j == b + i - 1  : print('*',end='')
        else :print('.',end='')
    print('')
    
