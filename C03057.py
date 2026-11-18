def m6(a):
    a = a.replace("5","6")
    return a
def m5(a):
    a = a.replace("6","5")
    return a
n = int(input())
for i in range(n):
    a , b = map(str,input().split())
    x = int(m6(a)) + int(m6(b))
    y = int(m5(a)) + int(m5(b))
    print(y,x)