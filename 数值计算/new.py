import pylab as pl
import numpy as np


def lagrange(x, y, w):
    n = len(x)
    res = 0
    for i in range(n):
        temp = 1
        for j in range(n):
            if i != j: temp = temp * (w - x[j]) / (x[i] - x[j])
        res += temp * y[i]
    return res


x = [16, 9, 25]
y = [4, 3, 5]
lagrange(x, y, 10)

x1 = np.linspace(-5, 5, 20)
y1 = x1 ** 2 + np.random.uniform(-1, 1, 20)
x2 = [-3, 2, 3, -1]
y2 = []
for i in x2:
    y2.append(lagrange(x1, y1, i))
pl.plot(x1, y1, 'r')
pl.scatter(x2, y2)
pl.xlim(-6, 6)
pl.ylim(-5, 30)
pl.show()
