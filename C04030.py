def vt(a,l,r):
    p = a[r]
    i = l - 1
    for j in range(l,r):
        if a[j] < p:
            i += 1
            a[i] , a[j] = a[j] , a[i]
    a[i + 1], a[r] = a[r] , a[i + 1]
    return i + 1
def quick_sort(a,l,r):
    if l < r:
        p = vt(a,l,r)
        quick_sort(a,l,p-1)
        quick_sort(a,p+1,r)
z = int(input())
for z1 in range(1,z+1):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(f"Test {z1}:")
    quick_sort(a,0,n - 1)
    quick_sort(b,0,n - 1)
    f = [0] * (2*n)
    j_a = 0
    j_b = n - 1
    for i in range(2*n):
        if i % 2 == 0:
            f[i] = a[j_a]
            j_a += 1
        else: 
            f[i] = b[j_b]
            j_b -= 1
    print(*f) 