n = int(input())
a = [int(x) for x in input().split()]
even = []
odd = []
for i in range(n):
    if a[i] % 2 == 0 : even.append(a[i])
    else: odd.append(a[i])
for j in range(len(even)):
    print(even[j],end=" ")
print()
for j in range(len(odd)):
    print(odd[j],end=" ")