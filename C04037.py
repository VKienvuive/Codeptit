f = [0] * (100005)
f1 = [0] * (101)
n = int(input())
a = list(map(int,input().split()))
d = 0
for i in a:
    f[i] += 1
for i in a :
    if f[i] >= 2:
        f1[d] = i
        d += 1
        f[i] = 0
print(d)
for i in range(0,d):
    print(f1[i],end=" ")
        