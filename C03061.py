for _ in range(int(input())):
    s = input().strip()
    first, last = int(s[0]), int(s[-1])
    x = s[1:-1]
    
    if (first * 2 == last or last * 2 == first) and x == x[::-1]:
        print("YES")
    else:
        print("NO")