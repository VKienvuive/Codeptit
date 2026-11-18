a=[0]*(100001)
a[0]=1
a[1]=1
a[2]=2
a[3]=6
a[4]=24
a[5]=120
a[6]=720
a[7]=5040
a[8]=40320
a[9]=362880
def ktr(b):
    s = 0
    x = b
    while x > 0:
        s += a[x%10]
        x //= 10
    if s == b:
        return True
    return False
c , b= map(int,input().split())
if c > b : c , b = b , c
if b > 100000:
    b = 100000
for i in range(c,b+1):
    if ktr(i):
        print(i,end=" ")
