a , b = map(int,input().split())
c , d = map(int,input().split())
e , f = map(int,input().split())
k = a * b + c * d + e * f
x = int(k**0.5)
if x * x != k : print('NO')
else :
    if a > b : a ,b = b, a
    if c > d : c ,d = d, c
    if e > f : e ,f = f, e
    if x == b and b == d and f == d : print('YES')
    else:
        if d == x :
            b,d=d,b
            a,c=c,a
        if f == x :
            f,b=b,f
            a,e=e,a
        if b == x:
            a = x - a
            if c == a and e == a or c == a and f == a or e == a and d == a or d == a and f == a: print('YES')
            else : print('NO')
        else : print('NO')
