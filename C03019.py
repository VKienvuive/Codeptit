# abcba : tong = 2*(a + b) + c
# a != 0 : a có 9c , b có 10c , c có 1 cách (với mỗi 1 cặp a và b thì có 1 c)
# abccba : tong = 2*(a + b + c)
# a != 0 : 9 có 9c , 
n = int(input())
while n > 0:
    n -= 1
    a = int(input())
    if a == 2 : print(1)
    elif a % 2 == 0:
        d = 18 * (10**(a//2 - 2))
        print(d)
    else:
        d = 9 * (10**(a//2 - 1))
        print(d)