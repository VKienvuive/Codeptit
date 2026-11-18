M = 1300000
a = [0]*(M+1)
def snt():
    a[0]=a[1]=1
    for i in range(2,int(M**0.5)+1):
        if a[i]==0:
            for j in range(i*i,M+1,i):
                a[j]=1
snt()
n = int(input())
d = 0
for i in range(2,M+1):
    if d == n : break
    if a[i]==0:
        print(i)
        d+=1
