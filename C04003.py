def doixung(a):
    for i in range(len(a)):
        if a[i] != a[len(a) - i - 1] : return False
    return True
n = int(input())
for i in range(n):
    a = int(input())
    b = [int(x) for x in input().split()]
    if doixung(b): print("YES")
    else: print("NO")