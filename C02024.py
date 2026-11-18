def max1(a , b):
    if a >= b : return a
    return b
a , b = map(int,input().split())
c = max(a,b)
for i in range (1,a+1):
    if i <= b :
        for j in range (i,b+1):print(chr(64+j),end='')
        for k in range (i - 1 , 0 , -1):print(chr(64+k),end='')
    else:
        for j in range( b , 0, -1):print(chr(64+j),end='')
    print('')
