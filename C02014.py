n = int(input())
l = 1 
r = 2*n - 1 
for i in range(1,n+1):
	a = n 
	for j in range(1,2*n):
		if j < l:
			print(a,end='')
			a = a - 1
		elif j >= r :
			print(a,end='')
			a = a + 1
		else : print(a,end='')
	l = l + 1
	r = r - 1
	print('')
l -= 2
r += 2
for i in range(2,n+1):
	a = n
	for j in range(1,2*n):
		if j < l :
			print(a,end='')
			a -=1
		elif j >= r:
			print(a,end='')
			a += 1 
		else : print(a,end='')
	l -=1
	r+=1
	print('')
