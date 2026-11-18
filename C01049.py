T = int(input())
for _ in range(T):
    n = int(input())
    le = 0
    chan = 0
    
    while n > 0:
        k = n % 10
        if k % 2 == 0:
            chan += 1
        else:
            le += 1
        n //= 10
        
    print(le, chan)