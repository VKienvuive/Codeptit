import sys
MAX = 2000000
a = [0] * (MAX + 1)

def snt():
    i = 2
    while i * i <= MAX:
        if a[i] == 0:
            for j in range(i * i, MAX + 1, i):
                if a[j] == 0:
                    a[j] = i
        i += 1
        
    for i in range(2, MAX + 1):
        if a[i] == 0:
            a[i] = i

def tt(b):
    x = 0
    while b != 1:
        x += a[b]
        b //= a[b]
    return x

snt()
input_data = sys.stdin.read().split()
if input_data:
    T = int(input_data[0])
    tong = 0    
    for i in range(1, T + 1):
        n = int(input_data[i])
        tong += tt(n)
        
    print(tong)