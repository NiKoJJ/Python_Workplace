# 优化算法
import numpy as np
from 数据分析.scipy库学习 import fmin
def f(x): # 定义f(x)函数
    return x ** 2 + 10 * np.sin(x)
x = np.arange(-5, 5, 0.2)  # 生成随机数组
print(fmin(f,0))  # 利用fmin()函数来求极值
# plt.plot(x,f(x))  # 绘制x f(x)函数
# plt.show()

