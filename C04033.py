f = [0] * (101)
n = int(input())
a = list(map(int,input().split()))
for i in a :
    f[i] += 1
for i in a :
    if f[i] != 0:
        print(i,end=" ")
        f[i] = 0