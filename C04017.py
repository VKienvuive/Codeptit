f = [0] * (100001)
def snt():
    f[0] = f[1] = 1
    for i in range(2,int(100000**0.5)+1):
        if f[i] == 0:
            for j in range(i*i,100001,i):
                f[j] = 1
snt()
n = int(input())
a = [int(x) for x in input().split()]
d = 0
for i in a :
    if f[i] == 0: d += 1
print(d,end=" ")
for i in a:
    if f[i] == 0:
        print(i,end=" ")
    