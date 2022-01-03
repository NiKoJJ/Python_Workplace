import matplotlib.pyplot as plt
import numpy as np

# # 正弦曲线图 plot()
x=np.arange(-np.pi,np.pi,0.1)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,linewidth=2.0,linestyle='--',label='sin(x)')
plt.plot(x,y2,color='red',linestyle='-.',label='cos(x)')
plt.legend()  # 设置图例,注意引入label
plt.grid(True)  # 设置格网线
plt.xlim(-np.pi,np.pi)
plt.xlabel("x")  # 注意要用双引号，下同;对中文好像不支持哦？
plt.ylabel("y")
plt.title("function of sin() and cos()")
plt.show()

# 饼状图 pie()
data=np.random.randint(1,11,5)
labels=['A','B','C','D','E']  # 标签数与data个数要对应
plt.pie(data,labels=labels)  # pie()图绘制饼图
plt.axis('equal') # 设置x，y刻度一样，这样画出来的图才是圆形的
plt.legend()
plt.show()

# 散点图 scatter()
x=np.arange(-np.pi,np.pi,0.1)
y=np.sin(x)
plt.scatter(x,y,color='r',marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('scatter')
plt.show()

# 柱状图
y=[4,5,2,1,7,5,9,6]
x=np.arange(8)
plt.bar(x,height=y,color='cyan')
plt.show()