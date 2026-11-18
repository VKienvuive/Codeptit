n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
for i in range(m,len(a)):
    print(a[i],end=" ")
for i in range(m):
    print(a[i],end=" ")