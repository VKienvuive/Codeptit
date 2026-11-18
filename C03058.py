import math

t = int(input())
for j in range(t):
    n = int(input())
    res = 1
    for i in range(2, n + 1):
        res = (res * i) // math.gcd(res, i)
    print(res)