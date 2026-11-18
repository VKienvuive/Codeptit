f = [0] * (1001)
def snt():
	f[0] = f[1] = 1
	for i in range(2,int(1001**0.5) + 1):
		if f[i] == 0 :
			for j in range(i*i,1001,i):
				f[j] = 1
snt()
n = int(input())
for i in range(n):
	a = int(input())
	b = [int(x) for x in input().split()]
	for j in range(a):
		if f[b[j]] == 0:
			print(b[j],end = " ")
	print()