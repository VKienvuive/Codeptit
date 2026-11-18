def tt(a):
	if a < 0 : a = - a
	return a 
a , b = map(int,input().split())
if a == b:
	for i in range(a, 0 ,-1):
		for j in range(i,0,-1): print(j,end='')
		for k in range(2,b-i+2):print(k,end='')
		print('')
if a < b:
	for i in range(1,a+1):
		for j in range(b - i + 1,0,-1):print(j,end='')
		for k in range(2,i+1):print(k,end='')
		print('')
if a > b:
	for i in range(a,0,-1):
		if i >=  b:
			for j in range(i,i-b,-1):print(j,end='')
		else :
			for j in range(i,0,-1):print(j,end='')
			for k in range(2,b-i+2):print(k,end='')
		print('')
