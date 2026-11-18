a = int(input())
while a > 0 :
    a -= 1
    n = int(input())
    t = 0
    while n > 0 :
        t += n % 10
        n //= 10
    print(t)
