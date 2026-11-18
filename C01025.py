def max1( a , b ):
    if a > b : return a
    return b
def min1( a , b ):
    if a < b : return a
    return b
x1 , y1 , x2 , y2 = map(int, input().split())
x3 , y3 , x4 , y4 = map(int, input().split())
minx = min1(min1(min1(x1,x2),x3),x4)
miny = min1(min1(min1(y1,y2),y3),y4)
maxx = max1(max1(max1(x1,x2),x3),x4)
maxy = max1(max1(max1(y1,y2),y3),y4)
xx = maxx - minx
yy = maxy - miny
print(max1(xx**2,yy**2))
