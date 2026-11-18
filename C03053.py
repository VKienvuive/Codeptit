M = 10000
f = [0] * (M + 1)
def snt():
    f[0] = f[1] = 1
    for i in range(2,int(M**0.5)+1):
        if f[i] == 0:
            for j in range(i*i,M+1,i):
                f[j] = 1
snt()
n = int(input())
for i in range(n):
    a = int(input())
    for j in range(2,a // 2 + 1):
        if f[j] == 0 and f[a - j] == 0 : 
            print(j,a-j,end=" ")
    print()
