n, k = map(int, input().split())

d = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        j = i
        while j % 2 == 0:
            d += 1
            j //= 2

if d >= k:
    print("Yes")
else:
    print("No")