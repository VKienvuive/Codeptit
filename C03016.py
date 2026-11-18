def fibo(a):
    if a <= 1: return True
    f0 = 0
    f1 = 1
    for i in range(2, 100):
        fn = f0 + f1
        f0 = f1
        f1 = fn
        if a == fn: return True
    return False
n = int(input())
while n > 0:
    n -= 1
    a = int(input())
    if fibo(a): print("YES")
    else: print("NO")
