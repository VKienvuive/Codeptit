f=[0]*(1001)
def snt():
    f[0] = f[1] = 1
    for i in range(2,1001):
        if f[i] == 0:
            for j in range(i*i,1001,i):
                f[j] = 1
def fibo(a):
    if a <= 1 : return True
    f0 = 0
    f1 = 1
    for i in range(2,100):
        fn = f0 + f1
        f0 = f1
        f1 = fn
        if a == fn: return True
    return False
def tong(a):
    s = 0
    while a > 0:
        s += a % 10
        a //= 10
    return s
snt()
a , b = map(int,input().split())
if a > b: a , b = b , a
for i in range(a,b+1):
    if f[i] == 0 and fibo(tong(i)): print(i,end=" ")