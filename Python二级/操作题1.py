
# ###  计算两点之间的距离
# import math
# aList=[]
# s=input("输入四个数字（空格间隔）：")
# n=s.split(" ")
# x0=eval(n[0])
# y0=eval(n[1])
# x1=eval(n[2])
# y1=eval(n[3])
#
# d=(x0-x1)*(x0-x1)+(y0-y1)*(y0-y1)
# Distance=math.sqrt(d)
# print(f"两点间的距离为：{Distance}")


# ## 居中显示
# s=input("请输入字符串：")
#
# if len(s)<=20:
#     print("{:=^20}".format(s))
# else:
#     print(s)

# ## 十六进制居中显示 30宽度
# p=eval(input("输入一个数字："))
# print("{:\"^30x}".format(p))



# s=input("输入五个数字，逗号隔开：")
# n=s.split(",")
# aList=[]
# for i in range(5):
#     aList.append(eval(n[i]))
# print(aList)
#
# ## 同一行显示
# for j in aList:
#     print("{: ^10}".format(j),end="")
#



## 列表操作

# a=[1,2,3]
# b=[]
# s=input("输入一组数字：")
# n=s.split(" ")
# for j in range(3):
#     b.append(n[j])
# print(b)
# sum=0
# for i in range(3):
#     sum+=a[i]*eval(n[i])
# print(sum)

b=eval(input())
print(b)
