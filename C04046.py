n = int(input())
for i in range(n):
    a = int(input())
    b = list(map(int,input().split()))
    b.sort()
    min1 = 100000000000
    for j in range(a - 1):
        min1 = min(min1,abs(b[j] - b[j+1]))
    d = 0
    for j in range(a - 1):
        if abs(b[j] - b[j+1]) == min1 :
            d += 1
    print(min1,d)