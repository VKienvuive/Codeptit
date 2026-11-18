n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(m):
    for j in range(n):
        print(a[j] , b[j] , end = " ")
    print()