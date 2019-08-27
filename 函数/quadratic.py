import math
def quadratic(a,b,c):
    det=math.pow(b,2)-4*a*c
    if det<0:
        return 'no solution'
    div=2*a
    x1=(-b+math.sqrt(det))/div
    x2=(-b-math.sqrt(det))/div
    return (x1,x2)

