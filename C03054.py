f = ["-1"] * (10)
f[0] = f[8] = f[9] = "0"
f[1] = "1"
def check(a):
    s = ""
    for char in a :
        if f[int(char)] == "-1" : return "INVALID"
    c = - 1 
    for char in a :
        if f[int(char)] == "0":
            if c == 1 : s = s + f[int(char)] 
        elif f[int(char)] == "1":
            s = s + f[int(char)] 
            c = 1 
    if c == -1 : return "INVALID"
    return s 
a = int(input())
for i in range(a):
    print(check(input()))