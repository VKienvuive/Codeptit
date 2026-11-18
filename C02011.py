a , b = map(int,input().split())
d = 0 
for i in range(1,a + 1):
    if i <= b :
        for j in range(i,b+1):
            print(j,end='')
        for h in range (1,i):
            print(b-h,end='')
    else :
        for k in range(i,i - b ,-1):print(k,end='')
    print('')
