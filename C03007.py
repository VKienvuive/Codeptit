M = 1000000
c =[0]*(M+1)
def snt():
    c[0]=c[1]=1
    for i in range(2,int(M**0.5)+1):
        if c[i] == 0:
            for j in range(i*i,M+1,i):
                c[j]=1
def dn(a):
    x = str(a)
    k = x[::-1]
    k = int(k)
    if k == a:
        return True
    return False
snt()
n = int(input())
while n > 0:
    n -= 1 
    a , b = map(int,input().split())
    res = 0 
    for i in range(a,b+1):
        if c[i]==0 and dn(i):
            res += 1
            print(i,end=" ")
        if res == 10:
            res = 0
            print()
    print()