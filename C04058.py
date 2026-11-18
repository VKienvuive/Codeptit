f = [1] * (1001)
def snt():
    f[0] = f[1] = 0
    for i in range(2, int(1000 ** 0.5) + 1):
        if f[i]:
            for j in range(i * i, 1001, i):
                f[j] = 0
snt()
t = int(input())
while t > 0 :
    t -= 1
    n = int(input())
    a = list(map(int,input().split()))
    f1 = [0] * (1001)
    for x in a :
        f1[x] = 1 
    for i in range(2,1001) :
        if f[i] == 1 and f1[i] == 1 :
            print(i , end = " ")
    print()
