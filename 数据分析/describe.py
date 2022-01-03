"""
@time:2020/11/05
@author:nikojj
@describe:遥感统计与描述
"""
import numpy as np
import matplotlib.pyplot as plt
import sys


# 均值
def aver_value(array):
    sum = 0
    k = array.size
    (r, c) = array.shape
    for i in range(r):
        for j in range(c):
            sum = sum + array[i, j]
    aver = sum / k
    return aver


# 中位数
def mid_value(array):
    # n = array.size
    (r, c) = array.shape  # 行列数
    n = r * c
    ar = []
    k = 0
    for i in range(r):  # 转换为一维数组
        for j in array[i]:
            ar.append(j)
    for i in range(len(ar) - 1):
        for j in range(i + 1, len(ar)):
            if ar[i] > ar[j]:
                ar[i], ar[j] = ar[j], ar[i]
    if n % 2 == 0:  # 偶数
        return (ar[n // 2] + ar[n // 2 - 1]) // 2
    else:  # 奇数
        return ar[n + 1 // 2]


# 排序 对每一行的值进行排序
def sort_row_value(arr):
    (r, c) = arr.shape
    for i in range(r):  # 控制行数
        for j in range(c):  # 遍历每一行中的前一个数值
            for k in range(j + 1, c):  # 后一个数值
                if arr[i][j] > arr[i][k]:
                    arr[i][j], arr[i][k] = arr[i][k], arr[i][j]
    return arr


# 排序 对每一列进行排序
def sort_col_value(arr):
    (r, c) = arr.shape
    for j in range(c):  # 控制列数
        for i in range(r):  # 遍历每一行数据
            for k in range(i + 1, r):
                if arr[i][j] > arr[k][j]:
                    arr[i][j], arr[k][j] = arr[k][j], arr[i][j]
    return arr


# 众数
def most_value(array):
    (value, counts) = np.unique(array, return_counts=True)
    print(value)
    print(counts)
    d = dict(zip(value, counts))  # zip连接 创建字典
    print(d)
    max_c = max(counts)
    for k, v in d.items():
        if v == max_c:
            return k


# 方差 variance
def var_value(array):
    (r, c) = array.shape
    # 均值
    m = aver_value(array)
    # 累加
    s = 0
    for i in range(r):
        for j in array[i]:
            s = s + (j - m) ** 2  # 累加求平方和
    var = s / (r * c)
    return var


# 协方差 covariance
def cov_value(array1, array2):
    # 判断
    if array1.shape != array2.shape:
        print("二个数组大小不一致！")
        sys.exit(1)  # 退出 返回1
    (r, c) = array1.shape
    m1 = aver_value(array1)
    m2 = aver_value(array2)
    s = 0
    for i in range(r):
        for j in range(c):
            s = s + (array1[i][j] - m1) * (array2[i][j] - m2)
    cov = s / (r * c)
    return cov


# 相关系数
def correla(array1, array2):
    cov = cov_value(array1, array2)
    v1 = var_value(array1)
    v2 = var_value(array2)
    cor = cov / (np.sqrt(v1 * v2))
    return cor


# 直方图
def bar_fig(ar):
    (value, counts) = np.unique(ar, return_counts=True)  # 去除重复元素，并统计个数
    plt.bar(value, height=counts, color='y')
    plt.xlabel('value')
    plt.ylabel('frequency')
    # plt.legend()  # 图例
    plt.grid()
    plt.show()


# 累计直方图
def bar_fig_acc(ar):
    (value, counts) = np.unique(ar, return_counts=True)
    print(value)
    print(counts)
    print(counts[0])
    # 字典
    fre = {}
    fre[0] = counts[0]
    # 累加
    for i in range(1, len(counts)):
        fre[i] = fre[i - 1] + counts[i]
    # 通过字典来获取累积个数
    fre = list(fre.values())
    # 作图 value 与 fre 相对应
    plt.bar(value, fre / sum(counts))
    plt.xlabel('value')
    plt.ylabel('Cumulative frequency')
    plt.grid()
    plt.show()
    return fre


# 测试数据
ar1 = np.array([[1, 5, 9, 4], [3, 5, 6, 8], [7, 5, 1, 3]])
bar_fig_acc(ar1)
print(most_value(ar1))

ar2 = np.array([[2, 5, 7, 9], [2, 1, 5, 7], [3, 6, 8, 7]])
print(cov_value(ar1, ar2))
