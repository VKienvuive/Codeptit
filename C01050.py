a , b = map(int,input().split())
for i in range(b):
    for j in range(a):
         if i == 0 or i == b - 1 :
              print('*',end='')
         elif j == 0 or j == a - 1 : print('*',end='')
         else : print(' ',end='')
    print('')