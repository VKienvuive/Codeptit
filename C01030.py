a = int(input())
while a > 0 :
    a -= 1
    n= int(input())
    i = 2
    while i <= n :
        if n % i == 0:
            while n % i == 0 :
                print(i , end=' ')
                n //= i
        else : i += 1
    if ( n != 1) :print(n)
    print(' ')
