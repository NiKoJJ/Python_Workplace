from matplotlib import pyplot as plt
from sympy import *
from sympy.abc import x
import numpy as np


# 非线性方程
def F(x):
    F = 54 * (x ** 6) + 45 * (x ** 5) - 102 * (x ** 4) - 69 * (x ** 3) + 35 * (x ** 2) + 16 * x - 4
    return F


print(diff(F(x),x))  # 导函数

for x0 in np.arange(-2,2,0.1):
    i = 0
    x_list = [x0]  # 一个用来存储每一次迭代后的x
    re_list = [0]   # 存储方程的根
    print("------------------------------")
    print(f'当初始值为{x0}时，其迭代结果如下：')
    print("------------------------------")
    while True:
        if diff(F(x), x).subs(x, x0) == 0:  # 判断导数是否为零
            print(f"{x0}为函数F(x)的一个极值点")
            break;
        else:
            x0 = x0 - F(x0) / diff(F(x), x).subs(x, x0)
            x_list.append(x0)
        print(f'迭代值：{x_list}')
        if len(x_list) > 1:
            i += 1
            error = abs((x_list[-1] - x_list[-2]))
            if error < 10 ** (-6):
                print(f'第{i}次迭代后，误差小于10^(-10)')
                break;
        else:
            pass
    re_list.append(x0)
    print(f'所求的方程根为：{x0}')