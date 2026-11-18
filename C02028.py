n = int(input())
for i in range(1,2*n,2):
	for j in range(i,2*n,2): print(chr(64+j),end='')
	print()