f = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
n = int(input())
for i in range(n):
    a = int(input())
    d = 0
    for j in range(len(f) - 1 , -1 , -1):
        if a >= f[j] :
            x = a // f[j]
            d += x
            a = a - x * f[j]
    print(d)