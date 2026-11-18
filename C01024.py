n = int(input())
while n > 0:
    n -= 1
    a = int(input())
    kt = a % 10
    while a >= 10 :
        a //= 10
    if a == kt : print("YES")
    else : print("NO")
    
