n = int(input())
for i in range(n,1,-1):
	for j in range (i - 1,i + i -1):print(chr(64+j),end='')
	print()
print('@')