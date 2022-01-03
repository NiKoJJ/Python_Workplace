import random
# aDict={"Jack":"12456","Bob":"67874","Egg":"28940"}
# s=input("输入名字：")
# if s in aDict:
#     print("{} {} {}".format(s,aDict[s],random.randint(1000,9999)))
# else:
#     print("不存在！")


# names=input("键入各个同学的行业名称：")
# s=names.split()
# d={}
# for i in range(len(s)):
#     d[s[i]]=d.get(s[i],0)+1
# ls=list(d.items())
# ls.sort(key=lambda x:x[1],reverse=True)
# for k in range(len(ls)):
#     zy,num=ls[k]
#     print(f"{zy}:{num}")

schools=input("输入学校分类：")
s=schools.split()
d={}
for i in range(len(s)):
    d[s[i]]=d.get(s[i],0)+1  ## 为字典中添加元素
## 字典转为列表，对其进行排序显示
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)  ## 根据数量进行排序
for k in range(len(ls)):
    a,b=ls[k]
    print(f"{a}-{b}")