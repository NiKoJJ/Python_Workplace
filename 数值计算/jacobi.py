import numpy as np


# 迭代公式：X(k+1)=inv(D)*(L+U)*x(k)+inv(D)*b，其中inv(D)为D的逆矩阵
# A 系数矩阵 b 常数矩阵 k迭代次数
def Jfunction(A, b, k):
    n = A.shape[1]  # 获取阶数
    D = np.eye(n)  # 对角矩阵D
    D[np.arange(n), np.arange(n)] = A[np.arange(n), np.arange(n)]
    LU = D - A  # A=D-L-U 得到 L+U=D-A
    X = np.zeros(n)  # 初始值均取值为0
    for i in range(k):
        D_inv = np.linalg.inv(D)
        X = np.dot(np.dot(D_inv, LU), X) + np.dot(D_inv, b)  # dot()函数矩阵相乘
        print(f'第{i}次迭代结果为：\n{X}')
        egg = b - np.dot(A, X)
        print(f"此时的误差大小为：{np.linalg.norm(egg)}")
    return X


def CreatMartA(n):
    a = [3] * n
    d = np.diag(a)
    for i in range(n):
        for j in range(n):
            d[0, 1] = -1
            d[n - 1, n - 2] = -1
    for i in range(1, n - 1):
        d[i, i - 1] = -1
        d[i, i + 1] = -1
    return d


def CreateMartB(n):
    a = [1] * n
    a[0] = 2
    a[n - 1] = 2
    a = np.array(a)
    return a


A = CreatMartA(100)
b = CreateMartB(100)
k = 40
X = Jfunction(A, b, k);

# 迭代39次可以达到10^(-6)
