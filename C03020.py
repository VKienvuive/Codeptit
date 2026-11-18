def ktr(a):
    res = 0
    check = 0
    check1 = a 
    t = 0
    while a > 0:
        if a % 10 == 6: check = 1
        res = res * 10 + a % 10
        t += a % 10
        a //= 10
    if check == 0 : return False
    if res != check1 : return False
    if t % 10 == 8 : return True
    return False
a , b = map(int,input().split())
if a > b: a , b = b , a
for i in range(a,b+1):
    if ktr(i): print(i,end=" ")
