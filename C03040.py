def tong_chu_so(a):
    t = 0
    while a > 0 :
        t += a % 10
        a //= 10
    return t 
def smith(a):
    x = a 
    t = 0
    while x > 0 :
        t += x % 10
        x //= 10
    i = 2
    while i * i <= a:
        while a % i == 0:
            t -= tong_chu_so(i)
            a //= i
        i += 1
    if a != 1 : t -= tong_chu_so(a)
    if t == 0 : return True
    return False
a = int(input())
if(smith(a)):print("YES")
else:print("NO")