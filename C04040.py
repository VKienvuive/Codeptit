n = int(input())
for i in range(n):
    sum = 0
    max1 = -1
    b = int(input())
    a = list(map(int,input().split()))
    for j in a :
        sum += j
        if sum <= 0: sum = 0
        max1 = max(sum,max1)
    print(max1)