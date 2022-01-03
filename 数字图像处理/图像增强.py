import sys

sys.path.append('/爬虫项目练习/describe.py')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 利用PIL读取
# I=Image.open('D:/文献&资料/Image/均衡化前.png')
# I.show()
# I_array=np.array(I)
# print(I_array.shape)
# print(I_array)


# 利用 matplotlib.image 进行读取
I = mpimg.imread('D:/文献&资料/Image/图片1.jpg')
(h, w, c) = I.shape
print(I.shape)  # (h,w,c)
# plt.imshow(I)
# plt.axis('off')  # 关闭x y 轴上的数字
# plt.show()

# 灰度图
im_r = I[:, :, 0]  # 红色通道
plt.imshow(im_r, cmap='Greys_r')  # 灰度图像
print('----------------')
# print(im_r)
print(im_r.shape)
plt.show()


# # 直方图
# plt.hist(im_r)
# plt.show()
# db.bar_fig(im_r)
# # 累积直方图
# k=db.bar_fig_acc(im_r)
# print(k)

# 生成与数组元素一一对应的每个数组元素出现次数的数组，即建立元素次数与数组元素一一对应的关系
def value_to_nums(arr):
    (r,c)=arr.shape
    num=np.zeros((1,256),dtype=np.int)
    for i in range(r):
        for j in range(c):
            k=arr[i][j]+1
            num[1,k]=num[1,k]+1
    print(num)


value_to_nums(im_r)


