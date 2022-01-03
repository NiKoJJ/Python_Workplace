import matplotlib.pyplot as plt
from sympy import *
from sympy.abc import x
import numpy as np
from sympy.plotting import plot


def F(x):
    b=4*x
    F = (1-3/b)**(1/3)
    return F

plot(F(x))


print(diff(F(x),x).subs(x,1))  # 导函数
print(5**(1/3)/20)


x0=0.6
i = 1
x_list = [x0]  # 一个用来存储每一次迭代后的x
re_list = [0]  # 存储方程的根
print("------------------------------")
print(f'当初始值为{x0}时，其迭代结果如下：')
print("------------------------------")
while i<=4:
    if diff(F(x), x).subs(x, x0) == 0:   # 判断导数是否为零
        print(f"{x0}为函数F(x)的一个极值点")
        break;
    else:
        x0 = x0 - F(x0) / diff(F(x), x).subs(x, x0)
        x_list.append(x0)
    print(f'第{i}次迭代值：{x_list}')
    i+=1
re_list.append(x0)
print(f'所求的方程根为：{x0}')
print(solve(F(x)))
