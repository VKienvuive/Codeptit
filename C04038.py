n = int(input())
a = list(map(int,input().split()))
k = 1 
for i in range(n-1):
    min_1 = i 
    check = 0
    for j in range(i + 1 , n , 1):
        if a[j] < a[min_1]:
            min_1 = j
    a[i] , a[min_1] = a[min_1] , a[i]
    print(*a)