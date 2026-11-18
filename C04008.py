z = int(input())
for k in range(1,z+1):
    n , m , p = map(int,input().split())
    a = [int(x) for x in input().split()]
    b = [int(y) for y in input().split()]
    j = 0
    print(f"Test {k}:")
    for i in range(p + len(b)):
        if i < p :
            print(a[i],end=" ")
        elif i < p + len(b):
            print(b[j],end=" ")
            j += 1        
    while p < len(a):
        print(a[p],end=" ")
        p += 1
    print()