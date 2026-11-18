a , b = map(int,input().split())
for i in range(1,a + 1):
	if i == 1 : 
	    for j in range (1,  b + 1): print(j, end='')
	elif i <=b : 
		for j in range(i, 0,-1):
			print(j,end='')
		for k in range(2,b - i + 2): print(k,end='')
	else:
		for j in range(i,i - b, -1): print(j,end='')
	print('')
