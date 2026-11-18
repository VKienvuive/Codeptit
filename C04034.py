f = []
n = int(input())
for i in range(n):
    a = int(input())
    b = list(map(int,input().split()))
    vt = 0
    max1 = -1
    f = [] 
    for j in range(a - 1, - 1, - 1):
        if b[j] > max1:
            f.append(b[j])
            max1 = b[j]
    f.sort(reverse=True)
    print(*f)