n = int(input())
print(0,1,end=" ")
f0 = 0
f1 = 1
for i in range(3,n+1):
	fn = f1 + f0
	f0 = f1
	f1 = fn
	print(fn,end=" ")