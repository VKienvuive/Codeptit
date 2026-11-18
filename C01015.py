a , b , c = map( int , input().split())
if a == 0:
    print(f"{ - c / b :.2f}")
else :
    delta = b ** 2 - 4 * a * c
    if delta < 0 :
        print(" NO ")
    elif delta == 0 :
        print(f"{ - b / ( 2 * a ) :.2f}")
    else :
        print(f"{ ( - b + delta**0.5 ) / ( 2 * a ) :.2f}", f"{ (- b - delta**0.5) / ( 2 * a ) :.2f}")
