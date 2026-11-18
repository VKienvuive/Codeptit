n = int(input())
for i in range(0,n):
    a , b , c , d = map(int,input().split())
    if a - c == b - d : print("YES")
    else :print("NO")