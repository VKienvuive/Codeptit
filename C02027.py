n = int(input())
a = 1
for i in range(1,n+1):
	if i % 2 != 0:
		for j in range(a,a+i):print(chr(96+j),end=' ')
		a = a + i
	else :
		for j in range(a+i-1,a-1,-1):print(chr(96+j),end=' ')
		a = a + i
	print()