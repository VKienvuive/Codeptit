limit = 1000000
f = [0] * (limit + 1)
my_check = { 0 , 1 , 4, 6 ,8,9}
def check(x):
    while x > 0 :
        k = x % 10 
        if k in my_check : return False
        x //= 10
    return True    
def snt():
    f[0]=f[1]=1
    for i in range(2,int(limit**0.5)+1):
        if f[i]==0:
            for j in range(i*i,limit+1,i):
                f[j] = 1
    for i in range(2,limit+1):
        if f[i] == 0 :
            if not check(i): f[i] = 1
snt()
n = int(input())
for i in range(1,n+1):
    a , b = map(int,input().split())
    d = 0
    for j in range(a,b +1):
        if f[j] == 0 : d += 1
    print(d)