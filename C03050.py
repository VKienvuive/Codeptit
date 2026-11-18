n = int(input())
deg = [0] * (n + 1)

for i in range(n - 1):
    u, v = map(int, input().split())
    deg[u] += 1
    deg[v] += 1
print("Yes" if n == 1 or max(deg) == n - 1 else "No")