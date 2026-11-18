n = int(input())
for i in range (n):
    for j in range(n - i - 1 , 0 , -1):print('~',end='')
    for k in range(2,2*i+3,2):print(k,end='')
    for h in range(2*i,0,-2):print(h,end='')
    print('')
