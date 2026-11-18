n = int(input())
t = 1
while n > 0:
    t *= n % 10
    n //= 10
print(t)
