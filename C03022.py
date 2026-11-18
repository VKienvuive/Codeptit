f=[0]*(100001)
def snt():
    f[0]=f[1]=1
    for i in range(2,int(100001**0.5)+1):
        if f[i] == 0:
            for j in range(i*i,100001,i):
                f[j] = 1
def tong(a):
    t = 0
    while a > 0 :
        t += a % 10
        a //= 10
    if t % 5 == 0: return True
    return False
snt()
n = int(input())
d = 0  
for i in range(1,n+1):
    if f[i]==0 and tong(i):
        d += 1 
        print(i,end=" ")
print()
print(d)