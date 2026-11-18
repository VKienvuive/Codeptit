a , b = map(int,input().split())
if a > b :
    x = a
    a = b
    b = x
print ( (a + b) * (b - a + 1) // 2)
