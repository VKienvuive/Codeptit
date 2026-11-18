r, c = map(int, input().split())

for i in range(r):
    for j in range(c):
        val = min(c - 1, (r - 1 - i) + j)
        print(chr(65 + val), end="")
    print()

