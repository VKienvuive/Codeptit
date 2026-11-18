def to_chu_so(a):
    res = 0
    while a > 0 :
        res += a % 10
        a //= 10
    return res
a , b = map(int,input().split())
if to_chu_so(a) <= to_chu_so(b):print(a,b)
else : print(b,a)