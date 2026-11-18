f = [0] * (100001)
z = int(input())
for i in range(1,z+1):
    print(f"Test {i}:")
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in a :
        f[i] += 1
    for i in a:
        if f[i] != 0:
            print(f"{i} xuat hien {f[i]} lan")
            f[i] = 0