n =int(input())
while n > 0 :
    n -= 1
    a = int(input())
    k = int(a**0.5)
    if k * k == a : print("YES")
    else : print("NO")
