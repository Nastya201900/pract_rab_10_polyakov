from math import sin
def f(x):
    return x * x * x - 8 * x + 1 - 5 * sin(x)
eps = 0.001
a = -100
while a <= 100:
    while (f(a) * f(a + 0.1) > 0) and (a <= 100):
        a = a + 0.1
    if (f(a)  * f(a + 0.1) <0):
        print('Интервал [', a, ';', a + 0.1, ']')
        x = a
        delta = 2 * eps
        while f(x) * f(x + delta) > 0:
            x = x + delta
        print('Решение: ','{:6.3f}'.format(x + eps))
        a = a + 0.1