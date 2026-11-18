n = int(input())
for i in range(n):
    for j in range(i + 1):
        if i == 0 or i == n - 1: print('*',end='')
        elif j > 0 and j < i : print('.',end='')
        else : print('*',end='')
    print('')
