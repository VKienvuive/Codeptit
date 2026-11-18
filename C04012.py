f = [0] * (101)
n = int(input())
a = [int(x) for x in input().split()]
for i in range(n):
    f[a[i]] += 1
for i in a :
    if f[i] > 1:
        print(i,end=" ")
        f[i] = 0
