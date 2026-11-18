def kt(a):
	if a == 0 or a == 1: return True
	f1 = 0
	f2 = 1
	for i in range(2,44):
		fn = f1 + f2
		f1 = f2 
		f2 = fn
		if a == fn: return True
	return False
n = int(input())
if kt(n): print(1)
else: print(0)