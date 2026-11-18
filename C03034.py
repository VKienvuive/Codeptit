def chia2(a):
    if a % 2 != 0 : return 0
    if a == 2 : return 1
    tonguoc = 1
    tongle = 1
    i = 2
    while i * i <= a:
        mu = 0
        while a % i == 0 :
            mu += 1
            a //= i
        if mu != 0:
            tonguoc *= (mu+1)
            if i > 2 :
                tongle *=(mu+1)
        i += 1
    if a > 1 :
        tongle *= 2
        tonguoc *= 2
    return tonguoc - tongle
n = int(input())
for i in range(1,n+1):
    a = int(input())
    print(chia2(a))