"""""
truong hop so buoc di la le (2k - 1):
d = 1 , 2 ,3 , ...  k - 1 , k , k - 1 , .. 3, 2, 1
dmax = 2 * (1 + 2 + .. + k - 1) + k = 2 * (k-1)*k /2 + k = k^2
=> khoang cach k ^ 2 can 2k - 1 buoc 
truong hop so buoc di la so chan 2k :
d = 1, 2, 3 ,...  , k , k , k - 1 , ... ,1
dmax = 2 * (1 + 2 + .. + k) =  2 * k(k + 1) / 2 = k^2 + k
=> khoang cach k^2 + k can 2k buoc
"""
import sys

for line in sys.stdin:
    data = line.split()
    
    if len(data) < 2:
        continue
        
    x = int(data[0])
    y = int(data[1])
    
    d = abs(y - x)
    
    if d == 0:
        print(0)
    else:
        k = int(d ** 0.5)
        if d == k * k:
            print(2 * k - 1)
        elif d <= k * k + k:
            print(2 * k)
        else:
            print(2 * k + 1)