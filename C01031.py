n = int(input())
i = 2
while i < n :
    if n % i == 0:
        while n % i == 0:
            print(str(i)+'x',end='')
            n //= i
            if n == i :
                print(n)
                n = 1
                break
    else :i += 1
if n != 1 : print(n)
