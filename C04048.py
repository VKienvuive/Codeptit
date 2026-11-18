
n = int(input())
m = int(input())
k = int(input())
lamps = list(map(int, input().split()))
lit = [False] * (n + 1)
for pos in lamps:
    start = max(1, pos - k)
    end = min(n, pos + k)
    for j in range(start, end + 1):
        lit[j] = True
        
ans = 0
i = 1
while i <= n:
    if not lit[i]:
        ans += 1
        new_pos = i + k
        start = max(1, new_pos - k)
        end = min(n, new_pos + k)
        for j in range(start, end + 1):
            lit[j] = True
        i = end + 1
    else:
        i += 1
        
print(ans)
