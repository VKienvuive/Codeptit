n = int(input())
a = list(map(int,input().split()))
k = 1
for i in range(n - 1):
    check = 0
    for j in range(i+1,n,1):
        if a[i] > a[j] :
            check = 1
            a[i], a[j] = a[j] , a[i]
    if check == 1:
        print(f"Buoc {k}:",end=" ")
        print(*a)
        k += 1