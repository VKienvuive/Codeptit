n = int(input())
for i in range(n):
    b = int(input())
    a = [int(x) for x in input().split()]
    for j in range(b):
        if a[j] % 2 == 0:
            print(a[j],end=" ")
    print()