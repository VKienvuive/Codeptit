n = int(input())
nam = 0
tuan = 0
if n >= 365 :
    nam = n // 365
    n = n - nam * 365
if n >= 7 :
    tuan = n // 7
    n = n - tuan * 7
print ( nam , tuan , n )
