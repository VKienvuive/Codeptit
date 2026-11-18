n = int(input())
while n > 0 :
    n -= 1
    a = int(input())
    print(f"{a} = ",end ="")
    i = 2
    while i * i <= a :
        mu = 0 
        while a % i ==  0 :
            a //= i
            mu += 1
        if mu != 0 :
            print(f"{i}^{mu}",end="")
            if a > 1 : print(" * ",end="")
        i += 1
    if a > 1 : print(f"{a}^1",end="")
    print()