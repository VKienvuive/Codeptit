n = int(input())
print(1)
a = 2
for i in range (1,n):
    if i % 2 != 0:
        for j in range( a + i , a - 1 , -1 ): print(j,end=' ')
        a = a + i + 1
    else:
        for j in range(a, a + i + 1): print(j,end=' ')
        a = a + i + 1
    print('')
            
