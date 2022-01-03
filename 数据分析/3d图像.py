from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# #定义坐标轴
# fig4 = plt.figure()
# ax4 = plt.axes(projection='3d')
#
# #生成三维数据
# xx = np.arange(-5,5,0.1)
# yy = np.arange(-5,5,0.1)
# X, Y = np.meshgrid(xx, yy)
# Z = np.sin(np.sqrt(X**2+Y**2))
#
# #作图
# ax4.plot_surface(X,Y,Z,alpha=0.3,cmap='winter')     #生成表面， alpha 用于控制透明度
# ax4.contour(X,Y,Z,zdir='z', offset=-3,cmap="rainbow")  #生成z方向投影，投到x-y平面
# # ax4.contour(X,Y,Z,zdir='x', offset=-6,cmap="rainbow")  #生成x方向投影，投到y-z平面
# # ax4.contour(X,Y,Z,zdir='y', offset=6,cmap="rainbow")   #生成y方向投影，投到x-z平面
# # ax4.contourf(X,Y,Z,zdir='y', offset=6,cmap="rainbow")   #生成y方向投影填充，投到x-z平面，contourf()函数
#
# #设定显示范围
# ax4.set_xlabel('X')
# ax4.set_xlim(-6, 4)  #拉开坐标轴范围显示投影
# ax4.set_ylabel('Y')
# ax4.set_ylim(-4, 6)
# ax4.set_zlabel('Z')
# ax4.set_zlim(-3, 3)
#
# plt.show()


# fig = plt.figure()  # 定义新的三维坐标轴
# ax3 = plt.axes(projection='3d')
#
# # 定义三维数据
# xx = np.arange(-8, 8, 0.2)  # row和cloum_stride为横竖方向的绘图采样步长，越小绘图越精细
# yy = np.arange(-8, 8, 0.2)
# X, Y = np.meshgrid(xx, yy)
# Z = (np.sin(X) + np.cos(Y))*0.6
#
# # 作图
# ax3.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
# # ax3.contour(X,Y,Z, zdim='z',offset=-1,cmap='rainbow')   #等高线图，要设置offset，为Z的最小值
# plt.show()

fig = plt.figure()  # 定义新的三维坐标轴
ax3 = plt.axes(projection='3d')

z1=[-65.9,-77.15,-75.25,-55.45,-66.95,-67,-71.85]
z2=[-77.7,-88.35,-84.45,-73.5,-65.05,-59.85,-85.75]
z3=[-73.95,-67.65,-77.25,-79.45,-82.55,-73.6,-69.55]
x=[4,2,2,4,4,2,1]
y=[4,4,6,6,2,2,3]

ax3.scatter(x,y,z1,c='r')
ax3.scatter(x,y,z2,c='g')
ax3.scatter(x,y,z3,c='y')

ax3.set_zlabel('Z')
ax3.set_xlabel('X')
ax3.set_zlabel('Y')
plt.show()