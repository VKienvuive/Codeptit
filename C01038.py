n = int(input())
k = len(str(n)) - 1
x = int(n % 10)
x1 = str(n)
y = int(x1[0])
print( n - x + y - y*(10**k) + x*10**k)
