from math import cos, sin, sqrt
def fb(x, v0, alfa):
    g = 9.81
    if v0 == 0: t = 0
    else: t = x/v0 * cos(alfa)
    return v0 * t * sin(alfa) - g * t * t / 2
a = 0
b = 10
h = 0.01
x = a
L1 = 0
alfa = 35.5
v0 = 12
while x < b:
    y1 = fb(x,v0,alfa)
    y2 = fb(x+h,v0,alfa)
    L1 = L1 + sqrt(h * h + (y2-y1) * (y2-y1))
    x = x + h
print('Длина кривой при ',alfa,' ', '{:10.3f}'.format(L1))
x = a
L2 = 0
alfa = 65.8
v0 = 12
while x < b:
    y1 = fb(x, v0, alfa)
    y2 = fb(x + h, v0, alfa)
    L2 = L2 + sqrt(h * h + (y2 - y1) * (y2 - y1))
    x = x + h
print('Длина кривой при ',alfa,' ', '{:10.3f}'.format(L2))
def S_PAR():
    a = 0
    b = 10
    h = 0.01
    x = a
    S = 0
    def f(x):
        return x**2
    while x < b:
        S += (f(x) + f(x+h))/2 * h
        x += h
    return print(S)
S_PAR()