a = int(input())
while a > 0 :
    a -= 1
    t = 2
    n = int(input())
    for i in range(2,int(n**0.5) + 1) :
        if n % i == 0:
            t *= i
            while n % i == 0 :
                n //= i
    t = t // 2 * n
    print(t)
