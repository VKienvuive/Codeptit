f = [0] * (10)
my_nt={"2","3","5","7"}
n = input()
for char in n:
    if char in my_nt:
        f[int(char)] += 1
for char in n:
    if f[int(char)] != 0 :
        print(char,f[int(char)])
        f[int(char)] = 0
