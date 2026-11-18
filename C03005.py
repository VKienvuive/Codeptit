def ucln(a,b):
    while b != 0:
        a, b = b , a % b 
    return a 
a , b = map(int,input().split())
for i in range(a,b+1):
    for j in range(i,b+1):
        if ucln(i,j)==1:
            print("(",end="")
            print(i,end="")
            print(",",end="")
            print(j,end="")
            print(")",end="")
            print()