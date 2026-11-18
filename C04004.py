f = [1,1]
def fibo():
    f1 = 1
    f2 = 1
    for i in range(3,93):
        f3 = f2 + f1
        f1 = f2 
        f2 = f3
        f.append(f3)
fibo()
n = int(input())
for i in range(n):
    a = int(input())
    print(f[a-1])
    