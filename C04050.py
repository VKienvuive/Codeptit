n , m = map(int,input().split())
a = [int(X) for X in input().split()]
b = [int(X) for X in input().split()]
f = [0] * (1000)
fa = [-1] * (1000)
fb = [-1] * (1000)
for i in a :
    f[i] = 1
    fa[i] = 1
for i in b :
    if f[i] == 1 :
        f[i] = 2
    fa[i] = 0
    fb[i] = 1
for i in range(1,1000) :
    if f[i] == 2 :
        print(i , end = " ")
print()
for i in range(1,1000) :
    if fa[i] == 1 :
        print(i , end = " ")
print()
for i in range(1,1000) :
    if fb[i] == 1 :
        if f[i] == 0 :
            print(i , end = " ")