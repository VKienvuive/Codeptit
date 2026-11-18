a = [-1] * 10
a[2] = a[3] = a[5] = a[7] = 0
n = int(input())
while n != 0:
    x = n % 10
    if a[x] != -1:
        a[x] += 1
    n //= 10        
for i in range(2, 8):
    if a[i] > 0:
        print(f"{i} {a[i]}")
