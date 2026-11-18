def max1(a,b):
	if a >= b : return a 
	return b
a , b = map(int,input().split())
c = max1(a,b)
for i in range (a):
	if i == 0:
		for j in range(b): print(chr(96+c),end='')
	elif i < b:
		for j in range(c,c - i - 1,-1):
			print(chr(96+j),end='')
		for k in range(i + 1,b):
			print(chr(96+c-i),end='')
	else :
			for h in range(c,a - b, -1): print(chr(96+h),end='')
	print('')