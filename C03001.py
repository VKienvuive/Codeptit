n = int(input())
for i in range(n):
	a = int(input())
	t = 0
	while a > 0:
		t += a % 10
		a = a //10
	if t % 10 == 0: print('YES')
	else : print('NO')