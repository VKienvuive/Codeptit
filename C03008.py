# p và 2^p - 1 là snt thì 2*(p-1)*(2^p-1) là số hoàn hảo 
s=[0]*(1000001)
def snt():
    s[0]=s[1]=1
    for i in range(2,int(1000000**0.5)+1):
        if s[i] == 0:
            for j in range(i*i,1000001,i):
                s[j]=1
def shh(a):
    for p in range(1,20):
        if s[p] == 0:
            x1 = 2**p - 1
            if s[x1] == 0:
                x2 = 2**(p-1)
                if (x2 * x1== a): return True
    return False
snt()
n = int(input())
for i in range(6,n):
    if shh(i):
        print(i,end=" ")
