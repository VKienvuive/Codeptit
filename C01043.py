def giathua(a):
    t = 1
    for i in range(1,a + 1):
        t *= i
    return t
a = input()
to = 0
for i in range(0,len(a)):
    to += giathua(int(a[i]))
if to == int(a) : print(1)
else : print(0)
