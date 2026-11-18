def snt(a):
    max1 = -1
    i = 2 
    while i*i <= a:
        if a % i == 0:
            max1 = i
            while a % i == 0:
                a //= i
        i += 1
    if a > 1:
        max1 = a
    return max1
n = int(input())
while n > 0:
    n -= 1
    a = int(input())
    print(snt(a))