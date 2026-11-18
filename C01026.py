def ngto(b):
    for i in range(2, int(b**0.5) + 1):
        if b % i == 0 : return 0
    return 1
a = int(input())
while a > 0:
    a -= 1
    n = int(input())
    if ngto(n) == 1 : print("YES")
    else : print("NO")

