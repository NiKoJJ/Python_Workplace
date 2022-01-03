import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection  # 模型比较和选择包
from sklearn.metrics import confusion_matrix  # 计算混淆矩阵，主要来评估分类的准确性
from sklearn.metrics import accuracy_score  # 计算精度得分

df=pd.read_csv('D:/文献&资料/Srtp/Data_Srtp.csv',encoding='utf-8')
df.head()
X=df.iloc[:,1:6] # 提取所有行，第一列至第五列的数据
y=df.classify  # 分类指标

X=np.array(X.values)
y=np.array(y.values)

from sklearn.model_selection import train_test_split
# 20%的测试样本，剩下为训练样本
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=2)
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)

from sklearn import neighbors  # 导入邻近算法库
# 定义一个knn算法分类器
# K临近算法的距离度量 p=2表示欧式距离
knn=neighbors.KNeighborsClassifier(algorithm='kd_tree',n_neighbors=4,weights='uniform',p=2)
knn.fit(X_train,y_train)

y_pred_knn=knn.predict(X_test)
print(y_pred_knn)

score=accuracy_score(y_test,y_pred_knn)  # 计算准确率
print(score)
con=confusion_matrix(y_true=y_test,y_pred=y_pred_knn)  # 混淆矩阵
print(con)
import seaborn as sns
sns.set()
f,ax=plt.subplots()
sns.heatmap(con,annot=True,ax=ax)
ax.set_title('confusion martix')
ax.set_xlabel('predict  (0-4)to(Srtp01-Srtp05)')
ax.set_ylabel('True  (0-4)to(Srtp01-Srtp05)')
plt.savefig('D:/文献&资料/Srtp/数据汇总/图像/KNN混淆矩阵.png',dpi=300)
plt.show()