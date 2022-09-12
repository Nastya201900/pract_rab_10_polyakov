from math import sqrt, pi
def fc(x):
    if abs(x) > 2:
        return 0
    return sqrt((1 - (x*x) / (2*2)) * 3 * 3)
L0 = pi * (3 * (2 + 3) - sqrt((3 * 2 + 3) * (2 + 3 * 3)))
a = -2
b = 2
h = 2
while True:
    L = 0
    x = a
    h = h/2
    while x < b:
        y1 = fc(x)
        y2 = fc(x+h)
        L = L + sqrt(h * h + (y2 - y1) * (y2 - y1))
        x = x + h
    L = L*2
    if (abs(L0-L) / L0 < 0.0001):
        break
print('Длина кривой ','{:10.3f}'.format(L))
print('Длина кривой по формуле','{:10.3f}'.format(L0))
print('Интервал дискретизации для 0.01% ', '{:8.5f}'.format(h))