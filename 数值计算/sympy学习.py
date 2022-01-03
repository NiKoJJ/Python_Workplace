import math
from sympy import *
from sympy import diff, expand, plot_implicit, Eq
from sympy.abc import x, y
from sympy.plotting import plot


def F(x):
    # return x ** 2 + y ** 2
    return (54 * (x ** 6) + 45 * (x ** 5) - 102 * (x ** 4) - 69 * (x ** 3) + 35 * (x ** 2) + 16 * x - 4)
plot(F(x))

for x in (solve(F(x))):
    print(x)

