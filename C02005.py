a , b = map(int,input().split())
for i in range (a):
    for j in range (b + i ):
        if j < i : print('~',end='')
        elif j <= b + i : print('*',end='')
    print('')
