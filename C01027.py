def ucln(a, b):
    while b > 0 :
        k = a % b
        a = b
        b = k
    return a
a = int(input())
while a > 0 :
    a -= 1
    x , y = map(int,input().split())
    print(ucln(x,y))
