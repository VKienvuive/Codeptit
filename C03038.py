def dem(a,b):
    t = 0
    for i in range(a,b+1):
        if i % a == 0:
            j = i
            while j % a == 0 :
                t += 1
                j //= a
    return t
n = int(input())
for i in range(0,n):
    a , b = map(int,input().split())
    print(dem(b,a))
