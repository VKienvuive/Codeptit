n = int(input())
print('@')
for i in range(2,n+1):
	print('@',end='')
	for j in range(2,2*i,2): print(chr(64+j),end='')
	for k in range(2*i-4,1,-2):print(chr(64+k),end='')
	print('@',end='')
	print()