n = int(input())
a = list(map(int,input().split()))
for i in range(n-1):
    check = 0
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j] , a[j + 1] = a[j + 1], a[j]
            check = 1
    if check == False : break
    print(f"Buoc {i+1}:",end=" ")
    print(*a)
    