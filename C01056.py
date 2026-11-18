def vv(a):
    k = a % 10
    a //= 10
    while a != 0:
        x = a % 10
        if k < x:
            return 0
        k = x
        a //= 10
    return 1
a = int(input())
for i in range(a):
    n = int(input())
    if vv(n) == 1: print("YES")
    else : print("NO")
