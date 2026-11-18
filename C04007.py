n , m = map(int,input().split())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
p = int(input())
j = 0
for i in range(p + len(b)):
    if i < p :
        print(a[i],end=" ")
    elif i < p + len(b):
        print(b[j],end=" ")
        j += 1        
while p < len(a):
    print(a[p],end=" ")
    p += 1
    