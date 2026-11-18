M = 30000
f = [0] * (M + 1)
z = int(input())
while z > 0:
    z -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in a :
        f[i] += 1
    fmax = max(f)
    for i in a :
        if f[i] == fmax:
            print(i,end=" ")
        f[i] = 0
    print()
    