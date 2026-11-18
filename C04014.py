f = [0] * (101)
n = int(input())
a = [int(x) for x in input().split()]
for i in a:
    f[i] += 1
for i in a:
    if f[i] != 0:
        print(i,f[i])
        f[i] = 0