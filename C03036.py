def tn(a):
    x = str(a)
    x = x[::-1]
    x = int(x)
    if a == x : return True
    return False
my_le = {0,2,4,6,8}
def check1(a):
    if not tn(a): return False
    t = 0
    while a > 0:
        k = a % 10
        if k in my_le : return False
        t += k
        a //= 10
    if t % 2 == 0 : return False
    return True
n = int(input())
for i in range(0,n):
    a = int(input())
    if check1(a):print("YES")
    else: print("NO")