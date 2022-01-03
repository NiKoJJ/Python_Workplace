import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from sklearn.gaussian_process import GaussianProcessRegressor
a=np.random.random(50).reshape(50,1)
b=a*2+np.random.random(50).reshape(50,1)
plt.scatter(a,b,marker = 'o', color = 'r', label='3', s = 15)
plt.show()

gaussian=GaussianProcessRegressor()
fiting=gaussian.fit(a,b)
c=np.linspace(0.1,1,100)
d=gaussian.predict(c.reshape(100,1))
plt.scatter(a,b,marker = 'o', color = 'r', label='3', s = 15)
plt.plot(c,d)
plt.show()




df=pd.read_csv('D:/文献&资料/Srtp/Data_Srtp.csv',encoding='utf-8')
df.head()
X=df.iloc[:,1:6] # 提取所有行，第一列至第六列的数据
y=df.classify  # 分类指标

X=np.array(X.values)
y=np.array(y.values)

print(X)
print("============")
print(y)