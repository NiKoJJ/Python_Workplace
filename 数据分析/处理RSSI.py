"""
describe the RSSI DataFrame
@time:2020/10/30
@author:nikojj
@file:the data of srtp's RSSI
"""
from math import sqrt

import pandas as pd
from numpy import mean


def read1_csv():
    """
     - 读取单个文件
    """
    df = pd.read_csv('C:/ProgramData/PassMark/WirelessMon/张A-srtp02.txt')
    print(df)

    y1 = df['Strength(dBm)']  # 读取RSSI强度列
    for i in range(0, 20):
        print("第”+i+“次所测的RSSI为：" + str(y1[i]))

    y2 = y1.head(20)  # 取前20行数据
    df_de = y2.describe()
    '''
      高斯滤波 RSSI范围 [0.15σ+μ，3.09σ+μ]
    '''
    for i in range(0, 20):
        chafang = 0
        chafang = (y1[i] - df_de['mean']) * (y1[i] - df_de['mean']) + chafang
        deta = sqrt(chafang / 20)
    print("高斯滤波derta为：" + str(deta))
    niu = df_de['mean']

    a = 0.15 * deta + niu - 1
    b = 3.09 * deta + niu + 1
    print("区间范围" + str(int(a)) + "  " + str(int(b)))

    select_y = []
    for i in range(0, 20):
        if int(a) <= y1[i] <= int(b):
            print(y1[i])
            select_y.append(y1[i])
    print(select_y)
    print(select_y)
    print(mean(select_y))
    df_de['mean'] = mean(select_y)  # 用滤波后的均值代替滤波前的均值
    df_de.to_csv('out.csv')
    print(df_de)



def read2_csv():
    """
     - 利用循环读取一系列文件
     - 一个特征点对5个AP点
    """
    for i in range(1, 6):  # 遍历文件 5个RSSI文件分别对应5个AP
        i = str(i)  # 字符化
        df = pd.read_csv('C:/ProgramData/PassMark/WirelessMon/张E-srtp0' + i + '.txt')
        y1 = df['Strength(dBm)']
        y2 = y1.head(20)
        df_de = y2.describe()
        df_de.to_csv('D:/文献&资料/Srtp/result/read2_csv/outE' + i + '.csv')  # 生成一个特征点所对应的5个文件

    df1 = pd.read_csv('D:/文献&资料/Srtp/result/read2_csv/outE1.csv')
    df2 = pd.read_csv('D:/文献&资料/Srtp/result/read2_csv/outE2.csv')
    df3 = pd.read_csv('D:/文献&资料/Srtp/result/read2_csv/outE3.csv')
    df4 = pd.read_csv('D:/文献&资料/Srtp/result/read2_csv/outE4.csv')
    df5 = pd.read_csv('D:/文献&资料/Srtp/result/read2_csv/outE5.csv')

    df_s = pd.concat([df1, df2, df3, df4, df5], keys=['S1', 'S2', 'S3', 'S4', 'S5'],
                     names=['Group', 'row'], axis=1).reset_index()  # axis默认为0 则生成文件竖排
    df_s.to_csv('D:/文献&资料/Srtp/result/read2_csv/srtpE_5AP.csv', index=False)


def read3_csv():
    """
     - 将A B C D E F G 7个点 各自所测得的5组数据进行归纳，将生成的5个.csv文件汇总成一个文件
    """
    for k in range(7):
        strs = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        for i in range(1, 6):  # 遍历文件
            df = pd.read_csv('C:/ProgramData/PassMark/WirelessMon/张' + strs[k] + '-srtp0' + str(i) + '.txt')  # 遍历读取
            y1 = df['Strength(dBm)']
            y2 = y1.head(20)
            df_de = y2.describe()

            '''
                  高斯滤波 RSSI范围 [0.15σ+μ，3.09σ+μ]
                '''
            for j in range(0, 20):
                chafang = 0
                chafang = (y1[j] - df_de['mean']) * (y1[j] - df_de['mean']) + chafang
                deta = sqrt(chafang / 20)
            # print("高斯滤波derta为：" + str(deta))
            niu = df_de['mean']

            a = 0.15 * deta + niu - 1
            b = 3.09 * deta + niu + 1
            print("区间范围" + str(int(a)) + "  " + str(int(b)))

            select_y = []
            for r in range(0, 20):
                if int(a) <= y1[r] <= int(b):
                    print(y1[r])
                    select_y.append(y1[r])

            df_de['mean'] = mean(select_y)  # 用滤波后的均值代替滤波前的均值

            df_de.to_csv('D:/文献&资料/Srtp/result/read3_csv/out' + strs[k] + str(i) + '.csv')

        df1 = pd.read_csv('D:/文献&资料/Srtp/result/read3_csv/out' + strs[k] + '1.csv')
        df2 = pd.read_csv('D:/文献&资料/Srtp/result/read3_csv/out' + strs[k] + '2.csv')
        df3 = pd.read_csv('D:/文献&资料/Srtp/result/read3_csv/out' + strs[k] + '3.csv')
        df4 = pd.read_csv('D:/文献&资料/Srtp/result/read3_csv/out' + strs[k] + '4.csv')
        df5 = pd.read_csv('D:/文献&资料/Srtp/result/read3_csv/out' + strs[k] + '5.csv')
        df_s = pd.concat([df1, df2, df3, df4, df5], keys=['S1', 'S2', 'S3', 'S4', 'S5'],
                         names=['Group', 'row'], axis=1).reset_index()  # 将上面生成的5个文件拼接到一个文件中
        df_s.to_csv('D:/文献&资料/Srtp/result/汇总_csv/汇总' + strs[k] + '.csv', index=False)


def delete_dBm():
    """
     - 对汇总的5个文件分别除去'Strength(dBm)'行、每个S1-5列中第一列索引
    """
    for i in range(7):
        St = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        df = pd.read_csv('D:/文献&资料/Srtp/result/汇总_csv/汇总' + St[i] + '.csv')
        df1 = df.drop(columns=['index', 'S1', 'S2', 'S3', 'S4', 'S5'])  # 除去 每个S的索引列
        df1 = df1.drop(index=0)  # 除去‘Strength’列
        df1.index = ['count', 'mean', 'std', 'min', '25%-value', '50%-value', '75%-value', 'max']
        df1.to_csv('D:/文献&资料/Srtp/result/汇总' + St[i] + '_result.csv')


def read_mean_value():
    """
    :return: 方法一
    """
    # St = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # for i in range(7):
    #     mdf = pd.read_csv('D:/文献&资料/Srtp/result/汇总' + St[i] + '_result.csv')
    #     print(mdf)
    #     row_mean = mdf.iloc[1]
    #     mean = row_mean.T
    #     print(mean)
    #     mean.to_csv('D:/文献&资料/Srtp/result/mean_value/mean' + St[i] + '_result.csv')
    #
    # df1 = pd.read_csv('D:/文献&资料/Srtp/result/mean_value/meanA_result.csv')
    # df2 = pd.read_csv('D:/文献&资料/Srtp/result/mean_value/meanB_result.csv')
    # df3 = pd.read_csv('D:/文献&资料/Srtp/result/mean_value/meanC_result.csv')
    # df4 = pd.read_csv('D:/文献&资料/Srtp/result/mean_value/meanD_result.csv')
    # df5 = pd.read_csv('D:/文献&资料/Srtp/result/mean_value/meanE_result.csv')
    # df6 = pd.read_csv('D:/文献&资料/Srtp/result/mean_value/meanF_result.csv')
    # df7 = pd.read_csv('D:/文献&资料/Srtp/result/mean_value/meanG_result.csv')

    # df_s = pd.concat([df1, df2, df3, df4, df5, df6, df7], keys=['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    #                  names=['Group', 'row'], axis=1).reset_index()  # 将上面生成的7个文件拼接到一个文件中

    # df_s.to_csv('D:/文献&资料/Srtp/result/mean/mean_未剔除冗余.csv', index=False)
    # mdf1 = pd.read_csv('D:/文献&资料/Srtp/result/mean/mean_未剔除冗余.csv')
    # mdf1 = mdf1.drop(index=[0, 1], columns=['index', 'A', 'B', 'C', 'D', 'E', 'F', 'G'])
    # mdf1.index = ['srtp01', 'srtp02', 'srtp03', 'srtp04', 'srtp05']
    # mdf1.to_csv('D:/文献&资料/Srtp/result/mean/mean_result.csv')

    """
        :return: 方法二
    """
    St = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for i in range(7):
        with open('D:/文献&资料/Srtp/result/汇总' + St[i] + '_result.csv', 'r', encoding='utf-8') as f:  # 读取文件路径
            reads = f.readlines()
            for index, info in enumerate(reads):
                if index == 2:
                    print(info)
                    with open('D:/文献&资料/Srtp/result/mean/mean_result1_未整合.csv', 'a+',   # 追写模式 注意结果会逐步累积
                              encoding='utf-8') as result:  # 新建路径
                        res = info
                        result.write(res)
                    result.close()
        f.close()
    mdf = pd.read_csv('D:/文献&资料/Srtp/result/mean/mean_result1_未整合.csv', header=None,
                      names=['srtp01', 'srtp02', 'srtp03', 'srtp04', 'srtp05'])  # 添加列索引
    mdf.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    mdf.to_csv('D:/文献&资料/Srtp/result/mean/mean_result1_整合后.csv')


if __name__ == '__main__':
    read1_csv()
    # read2_csv()
    # read3_csv()
    # delete_dBm()
    # read_mean_value()
