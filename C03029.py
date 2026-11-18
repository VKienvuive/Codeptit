def ktr(n):
	x = int(n)
	if x % 2 != 0 : return False
	if "5" in n or "3" in n or "1" in n or "7" in n or "9" in n : return False
	return True
n = int(input())
while n > 0:
	n -= 1
	a = input()
	if ktr(a):print("YES")
	else : print("NO")