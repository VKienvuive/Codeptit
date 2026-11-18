T = int(input())

for _ in range(T):
    N = int(input())
    
    sq_set = {int(x)**2 for x in input().split()}
    
    arr = sorted(sq_set)
    n = len(arr)
    
    found = False
    
    for i in range(n - 1, 1, -1):
        c = arr[i]
        limit = c // 2 
        
        for j in range(i):
            a = arr[j]
            
            if a > limit:
                break
            
            if c - a in sq_set:
                found = True
                break
                
        if found:
            break
            
    print("YES" if found else "NO")