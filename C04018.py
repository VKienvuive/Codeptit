z = int(input())
while z > 0:
    z -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    d = 0
    for i in range(n - 1):
        if a[i] == a[i + 1]: d += 1
    print(d)