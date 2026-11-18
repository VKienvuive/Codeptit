def ucln(a,b):
	while b > 0:
		cnt = a % b 
		a = b
		b = cnt 
	return a
n = int(input())
while n > 0:
	n -= 1
	a , b = map(int,input().split())
	print(a*b//ucln(a,b),ucln(a,b))