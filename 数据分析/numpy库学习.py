import numpy as np

array=np.array([[5,2,3,4],[8,3,4,5],[1,4,5,6]])
print(array)
print(array.shape)
print(array.size)
print(array.dtype)

# 创建数组的特定方式
a=np.arange(10)  # np.arange创建等差数组
print(a)
b=np.linspace(0,2,5)  # 创建指定范围内步长均匀的数组
print(b)
c=np.zeros((2,3))  # 创建元素均为0的数组
print(c)
d=np.eye(5)  # 创建单位矩阵
print("-----------")
print(d)

e=np.random.random((3,4))  # 创建随机矩阵，有时需要seed()种子进行保存
print(e)

# 基础数组运算
ar1=np.arange(10)
ar2=np.arange(1,11)
print(ar1*2)
print(ar1+ar2)

# 数组索引
print(ar1[5])
print(ar1[3:6])
print(array[0,1:4])  # 索引二维数组 第一行从下标为1到下标为3

# 数组的统计分析
array_sort=np.sort(array)  # 数组总和
array_sum=np.sum(array)  # 数组总和
array_mean=np.mean(array)  # 数组均值
array_std=np.std(array)  # 数组方差
print(array_sort)
print(array_sum)
print(array_mean)
print(array_std)

# 数组的矩阵操作
arr=np.arange(3)  # 创建0-2之间的等差数组，默认步长为1
matr=np.mat("1 2 3;4 5 6;7 8 9")  # 使用mat函数创建矩阵
print(arr)
print(matr)
print(np.dot(arr,matr))  # 利用dot进行矩阵相乘

