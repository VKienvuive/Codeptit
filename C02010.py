a , b = map(int,input().split())
d = 0 
for i in range(1,a + 1):
    for j in range(i,b + 1):
        print(j,end='')
    if i > 1:
        if i > b :
            print(i,end='')
            for k in range(b - 1 , 0, -1): print(k,end='') 
        else :
            for k in range(i - 1 , 0, -1): print(k,end='')
    print('')
