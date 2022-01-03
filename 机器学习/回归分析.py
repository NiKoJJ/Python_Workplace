import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import numpy as np
import pandas as pd

# DataFrame数据集
df = pd.read_csv('D:/文献&资料/Srtp/Data_Srtp.csv', encoding='utf-8')
print(df.head())
# 直方图
df.hist(xlabelsize=12, ylabelsize=12, figsize=(12, 7))
plt.savefig('D:/文献&资料/Srtp/数据汇总/直方图.jpg', dpi=300)
plt.show()
# 密度图
df.plot(kind='density', subplots=True, layout=(3, 2), sharex=False, fontsize=8, figsize=(12, 7))
plt.savefig('D:/文献&资料/Srtp/数据汇总/密度图.jpg', dpi=300)
plt.show()
# 箱线图
df.plot(kind='box', subplots=True, layout=(3, 2), sharex=False, sharey=False, fontsize=8, figsize=(12, 7))
plt.savefig('D:/文献&资料/Srtp/数据汇总/箱线图.jpg', dpi=300)
plt.show()
# 相关系数热力图
names = ['srtp01', 'srtp02', 'srtp03', 'srtp04', 'srtp05']  # 变量
correlations = df.corr()  # 计算变量之间的相关系数矩阵
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=0, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, 5, 1)
ax.set_xticks(ticks)  # x刻度
ax.set_yticks(ticks)  # y刻度
ax.set_xticklabels(names)  # x轴标签
ax.set_yticklabels(names)  # y轴标签
plt.savefig('D:/文献&资料/Srtp/数据汇总/相关系数热力图.jpg', dpi=300)
plt.show()
# 散点图矩阵
scatter_matrix(df, figsize=(8, 8), c='r')
plt.savefig('D:/文献&资料/Srtp/数据汇总/散点图矩阵.jpg', dpi=300)
plt.show()
