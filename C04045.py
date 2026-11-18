import sys
def check(a):
    x = len(a)
    even = 0
    odd = 0
    for i in a:
        if i % 2 == 0: even += 1
        else : odd += 1
    if x % 2 == 0 and even > odd : return "YES"
    if x % 2 != 0 and even < odd : return "YES"
    return "NO"
n = int(input())
for i in range(n):
    a = list(map(int,input().split()))
    print(check(a))
