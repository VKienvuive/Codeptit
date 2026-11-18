def gcd(a,b):
    while b > 0:
        x = a % b
        a = b
        b = x 
    return a
n = int(input())
for i in range(1,n+1):
    a , b , c , d = map(int,input().split())
    if gcd(a,b) == gcd(d,c) : print("YES")
    else : print("NO")
