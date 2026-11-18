def gt(a):
    if a == 1 or a == 0 : return 1 
    return a * gt(a-1)
def pascal(a,b):
    return gt(a) / (gt(b) * gt(a - b))
n = int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print(int(pascal(i,j)),end=" ")
    print()
