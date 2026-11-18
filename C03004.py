a , b = map(int,input().split())
x = 0
k = a * b
while b > 0 :
    x = a % b 
    a = b
    b = x
print(a)
print(k // a)