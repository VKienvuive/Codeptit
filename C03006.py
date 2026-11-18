n = int(input())
k = 1
while ( n > 0):
    n -= 1
    a = int(input())
    print(f"Test {k}:",end=" ")
    i = 2 
    while (i <= a):
        if a % i == 0:
            print(i,end="")
            t = 0
            while (a % i == 0):
                t += 1
                a //= i
            print("(",end="")
            print(t,end="")
            print(")",end=" ")
        i += 1
    if a > 1: 
        print(a,end="")
        print("(1)",end="")
    k += 1
    print()
                