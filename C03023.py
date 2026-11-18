def tn(n):
    x = str(n)
    a = str(n)
    a = a[::-1]
    a = int(a)
    if a != n : return False
    if "9" in x : return False
    return True
n = int(input())
d = 0
for i in range(2,n+1):
    if tn(i) :
        d += 1
        print(i,end=" ")
print()
print(d)