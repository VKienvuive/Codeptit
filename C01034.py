a , b = map(int , input().split())
t = int(a**0.5)
if t * t != a: t += 1
dem = int(b**0.5) - t + 1
print(dem)
for i in range(t,int(b**0.5)+1):
    print(i*i)
