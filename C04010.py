n = int(input())
a = [int(x) for x in input().split()]
min1 = min(a)
min2 = 101
for i in a:
    if i != min1:
        min2 = min(min2,i)
print(min1,min2)