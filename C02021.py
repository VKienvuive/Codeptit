n = int(input())
for i in range(1,n+1):
    a = i
    b = i
    d = 1
    while a > 0 :
        a -= 1
        print(b,end=' ')
        b = b + n - d
        d += 1
    print('')
