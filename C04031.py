n = int(input())
for i in range(1,n+1):
    a = int(input())
    b = list(map(int,input().split()))
    f = [1] * (a + 1)
    for j in range(a - 1):
        if b[j] < b[j+1]:
            f[j + 1] = f[j] + 1
    max1 = max(f)
    print(f"Test {i}:")
    print(max1,end="")
    for j in range(a - max1 + 1):
        if f[j + max1 - 1] == max1:
            print()
            for k in range(max1):
                print(b[j + k],end=" ")
    print()