t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    def gen(pos, last, num):
        if pos == n:
            ans.append(num)
            return
        for d in range(last, 10):
            gen(pos + 1, d, num * 10 + d)
    gen(0, 1, 0)
    print(*ans)