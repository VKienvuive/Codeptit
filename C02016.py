n = int(input())
print(1)
for i in range(2,n+1):
    if i % 2 == 0:
        for j in range(2,2*i+1,2):print(j,end='')
    else:
        for j in range(1,2*i,2):print(j,end='')
    print('')
