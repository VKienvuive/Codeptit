f = [0] * (10001)
f1 = [0] * (100001)
def snt():
    f[0] = f[1] = 1
    for i in range(2,int(10000**0.5)+1):
        if f[i] == 0:
            for j in range(i*i,10001,i):
                f[j] = 1
snt()
z = int(input())
for i in range(1,z+1):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(f"Test {i}:")
    for j in a:
        if f[j] == 0:
            f1[j] += 1
    for j in range(2,10001):
        if f1[j] != 0:
            print(f"{j} xuat hien {f1[j]} lan")    
            f1[j] = 0
    