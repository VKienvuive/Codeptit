n = int(input())
t = 0
for i in range(1,int(n**0.5)+1):
    if n % i == 0:
        if i == n // i: t += i
        else : t += i + n//i
if t == 2*n : print(1)
else : print(0)
