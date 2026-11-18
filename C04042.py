n = int(input())
while n > 0:
    n -= 1
    count = {}
    x = 0
    b = int(input())
    a = list(map(int,input().split()))
    for i in range(b - 1 , -1 , -1):
        if a[i] not in count :
            count[a[i]] = 1
        else :
            x = a[i]
    if x != 0:print(x)
    else: print("NO")