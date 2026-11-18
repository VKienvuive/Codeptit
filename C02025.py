a , b = map(int,input().split())
print('@',end='')
for i in range (1,a+1):
    if i == 1 :
        for j in range(1,b): print(chr(64+j),end='')
    else:
        for j in range(i-1,b):print(chr(64+j),end='')
        if i <= b :
            for k in range(i-1,0,-1):print(chr(64+b-1),end='')
        else:
            for k in range(1,b+1):print(chr(64+b-1),end='')
    print('')
        
