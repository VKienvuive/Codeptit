import math

t = int(input())
for j in range(t):
    n,m = map(int,input().split())
    res = 1
    for i in range(n, m + 1):
        res = (res * i) // math.gcd(res, i)
    print(res)