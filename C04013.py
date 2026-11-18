f = [0] * (101)
h = []
n = int(input())
a = [int(x) for x in input().split()]
d = 0
for i in a:
    f[i] += 1
for i in a:
    if f[i] == 1: 
        h.append(i)
        f[i] = 0
print(len(h))
for i in h:
    print(i,end=" ")