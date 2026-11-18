tup = 0
tdown = 0
minu = 25001
mind = 25001
n = int(input())
for i in range(n):
    u , d = map(int,input().split())
    tup += u
    tdown += d
    minu = min(minu,u)
    mind = min(mind,d)
print(max(tup + mind,tdown + minu))
