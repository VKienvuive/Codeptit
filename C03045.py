def max1(a,b):
    if a >= b : return a
    return b
def uocnt(a):
    m1 = -1
    i = 2
    while i * i <= a:
        while a % i == 0 :
            m1 = max1(m1,i)
            a //= i
        i += 1
    if a > 1 : m1 = max1(a,m1) 
    return m1
n = int(input())
for i in range(1,n+1):
    a = int(input())
    print(uocnt(a))
    

