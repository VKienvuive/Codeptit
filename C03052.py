M = 1000000
f = [0] * (M + 1)
def snt():
    f[0] = f[1] = 1 
    for i in range(2,int(M**0.5)+1):
        if f[i] == 0 :
            for j in range(i*i,M+1,i):
                f[j] = 1
snt()
n = int(input())
for i in range(1,n+1):
    a , b = map(int,input().split())
    l = int(a**0.5)
    r = int(b**0.5)
    d = 0
    if a != l * l : l += 1
    for i in range(l,r+1):
        if f[i] == 0 : d += 1
    print(d)
