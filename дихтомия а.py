from math import sin, sqrt
e = 0.0001
def f(x):
    return x * x * x - 8 * x + 1 - 5 * sin(x)
gold = (sqrt(5) + 1)/2
a = -5
b = 5
while True:
    x1 = b-((b-a)/gold)
    x2 = a+((b-a)/gold)
    y1 = f(x1)
    y2 = f(x2)
    if y1<=y2: a = x1
    else: b = x2
    if abs (y2 - y1) < e:
        break
print('max = ', '{:0.3f}'.format((x1+x2) / 2), ',','{:0.3f}'.format((y1 + y1) / 2 ))
a = -5; b = 5
while True:
    x1 = b - ((b - a) / gold)
    x2 = a + ((b - a) / gold)
    y1 = f(x1)
    y2 = f(x2)
    if y1 >= y2: a = x1
    else: b = x2
    if abs (y2 - y1) < e:
        break
print('min = ', '{:0.3f}'.format((x1 + x2) / 2), ',','{:0.3f}'.format((y1 + y2) / 2))