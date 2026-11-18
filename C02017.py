n = int(input())
print(1)
for i in range(2,n+1):
    for j in range(1,2*i,2):print(j,end='')
    for k in range(2*i-3,0,-2):print(k,end='')
    print('')
