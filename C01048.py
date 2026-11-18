n = int(input())
even = 0
odd = 0

while n > 0:
    t = n % 10
    if t % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10

print(odd, even)