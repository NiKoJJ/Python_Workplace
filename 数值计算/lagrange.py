import numpy as np
import matplotlib.pyplot as plt


def F(x):
    F=1/(1+12*x**2)
    return F


#  x,y为对应的列表，w为所对应的插值节点的横坐标
def lagrange(x,y,w):
    n = len(x)
    res=0
    for i in range(n):
        temp = 1
        for j in range(n):
            if i!=j:
                temp = temp * (w-x[j]) / (x[i] - x[j])
        res += temp * y[i]
    return res

plt.figure(1)
w=[4,8,16,20,32,64]
X=np.linspace(-1,1,4)
Y=[]  # 存储原函数值
for x in X:
    Y.append(F(x))
YL=[]  # 存储lagrange数值
for k in X:
    YL.append(lagrange(X,Y,k))

plt.plot(X,Y,linestyle="--",label="Origin")
plt.plot(X,YL,color='r',label="Lagrange")
plt.scatter(X,YL,color='blue',marker='o',label='Lagrange Point')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.subplot(2,3,1)
plt.show()
