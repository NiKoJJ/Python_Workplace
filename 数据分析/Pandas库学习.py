import numpy as np
import pandas as pd

# series 和 DataFrame 会在 每一行赋予索引 每一列赋予标签

# I.创建序列 series
series = pd.Series(np.arange(2, 12))  # 序列series 通过索引标签的方式获取数据
print(series)
dr = {'a': 1, 'b': 2, 'c': 3, 'e': 5}
s2 = pd.Series(dr)
print(s2)

# II.创建DataFrame 一般由读写其他文件和数据库二创建 也可通过输入数据
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 8, 2]})
print(df)

df1 = pd.read_csv('D:/文献&资料/srtp.CSV')  # pd.read_csv读取本地文件
k = df1.head(15)  # 显示前15行数据
print(k, df1.index, df1.columns, df1.describe())  # 显示前15行、索引、列、基础的统计分析
select_df1 = df1.to_csv('D:/文献&资料/srtp1.CSV', columns=['SSID', 'MAC', 'Percentage(%)', 'Strength(dBm)'], index=False,header=True)

sortdf1 = df1.sort_values(by='Strength(dBm)')  # 按照某一值进行排序
print(sortdf1.head(24))

Tdf1 = df1.T
print(Tdf1.head(24))  # 转置

#  III.处理缺失值
df2 = pd.DataFrame({'A': [3, 5, 9, 1], 'B': [5, 7, 3, 1]})
print(df2['A'])
print(df2['B'])
df2['C'] = pd.Series([1, 2])
print(df2['C'])

df2_new = df2.dropna(how='any')  # dropna()函数去掉其值为NaN的行或列
print(df2)
print(df2_new)
