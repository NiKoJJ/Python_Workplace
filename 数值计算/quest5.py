import numpy as np
import matplotlib.pyplot as plt


def F(x):
    F = 1 / (1 + 12 * x ** 2)
    return F


#  x,y为对应的列表，w为所对应的插值节点的横坐标
def Lagrange(x, y, w):
    n = len(x)
    res = 0
    for i in range(n):
        temp = 1
        for j in range(n):
            if i != j:
                temp = temp* (w - x[j]) / (x[i] - x[j])
        res += temp*y[i]
    return res


X = [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003]
Y = [67.052, 68.008, 69.903, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777]  # 存储原函数值

X1=[1994, 1995, 1996, 1997]
Y1=[67.052, 68.008, 69.903, 72.024]
YL = []   # 存储lagrange数值
for k in X:
    YL.append(Lagrange(X, Y, k))
print(YL)
print(Lagrange(X,Y,2010))

plt.figure(1)
plt.plot(X, Y, linestyle="--", label="Origin")
# plt.plot(X, YL, color='r', label="Lagrange")
plt.scatter(X, YL, color='blue', marker='o', label='Lagrange Point')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
