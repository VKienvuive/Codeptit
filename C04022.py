n = int(input())
a = [int(x) for x in input().split()]
max1 = max(a)
max2 = -1 
for i in a:
    if i < max1:
        max2 = max(max2 , i)
print(max1,max2)