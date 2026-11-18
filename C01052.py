a = int(input())
for i in range(a):
    t = 0
    n = int(input())
    for j in range(1,int(n**0.5)+1):
        if n % j == 0 :
            if j % 2 == 0 : t += 1
            if n // j % 2 ==0: t += 1
            if j % 2 == 0 and j == n // j : t -= 1
    print(t)
                    
