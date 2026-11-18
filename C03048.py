def check(a):
    even = 0 
    odd = 0
    for i in range(0,len(a)):
        if int(a[i]) % 2 == 0 : even += 1
        else : odd += 1
    if even > odd and int(a[len(a)-1]) % 2 == 0 : return True
    return False
n = int(input())
for i in range(n):
    a = input()
    if check(a): print("YES")
    else : print("NO")