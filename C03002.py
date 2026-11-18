MAX = 1000000
a = [0]*(MAX +1)
def snt():
	a[0]=a[1]=1
	for i in range(2,int(MAX**0.5)+1):
		if a[i] == 0 :
			for j in range(i*i,MAX+1,i):
				a[j] = 1
snt()
n = int(input())
for i in range(2,n):
	if a[i]==0:
		print(i)