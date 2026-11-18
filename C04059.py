f = [None] * (94)
def fibo():
    f[0] = 0
    f[1] = 1
    for i in range(2, 94):
        f[i] = f[i - 1] + f[i - 2]
fibo()
n = int(input())
while n > 0 :
    n -= 1
    a , b = map(int,input().split())
    for i in range( a , b + 1) :
        print(f[i] , end = " ")
    print()