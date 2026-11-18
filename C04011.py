def check1(a,i):
    for j in range(i,-1,-1):
        if a[i] < a[j]: return False
    return True
b = int(input())
for j in range(b):
    n = int(input())
    a = [int(x) for x in input().split()]
    d = 1
    for i in range(1,n):
        if check1(a,i): d += 1
    print(d)