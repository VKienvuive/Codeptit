n = int(input())

f = []
for _ in range(n):

    t, d = map(int, input().split())
    f.append((t, d))
    

f.sort(key=lambda x: x[0])

time1 = 0
for t, d in f:
    if time1 < t:
        time1 = t
    
    time1 += d
    
print(time1)