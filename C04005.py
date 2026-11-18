n = int(input())
for i in range(n):
    a = int(input())
    b = [int(x) for x in input().split()]
    max1 = max(b)
    print(max1)
    for j in range(a):
        if b[j] == max1 :
            print(j,end=" ")
    print()