def vt(a,low,high):
    pivot  = a[high]
    i = low - 1
    for j in range(low,high):
        if a[j] < pivot:
            i += 1
            a[i] , a[j] = a[j] , a[i] 
    a[i + 1] , a[high] =  a[high] , a[i + 1]
    return i + 1 
def quick_sort(a,low,high):
    if low < high:
        pi = vt(a,low,high)
        quick_sort(a,low,pi-1)
        quick_sort(a,pi+1,high)
    
even = []
odd =[]
n = int(input())
a = list(map(int,input().split()))
quick_sort(a,0,n-1)
for i in range(n):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
print(*even,*odd)
