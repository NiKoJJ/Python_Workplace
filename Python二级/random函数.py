import random

## random.random() 生成0 <=n<1.0的一个随机数 [0,1)
rm1=random.random()
print(rm1)

## random.uniform(a,b) 生成一个指定范围的随机浮点数[a,b]
rm2=random.uniform(2,8)
print(rm2)

## random.randint(a,b)  生成一个指定范围内的整数 [a,b]
rm3=random.randint(3,19)
print(rm3)

## random.randrange(start,stop,step)  在生成的序列中获取一个随机数
rm4=random.randrange(0,19,3)
print(rm4)

## random.choice（sequence） 从序列中获取一个随机元素
rm51=random.choice("ILOVEPython")
rm52=random.choice(["Python","YYDS","Love"])
rm53=random.choice(("Python","yyda","love"))
print(f"{rm51}--{rm52}--{rm53}")

## random.shuffle(x)  将一个列表中的元素打乱
listA=[1,2,3,4,5,6,7,8,9]
random.shuffle(listA)
print(listA)

## random.sample() 从指定序列中随机获取指定长度的片段,并不修改原有序列
listB=[23,4,5,6,7,1,2,9]
sample=random.sample(listB,3)
print(sample)
print(listB)

## random.seed()
# 用于指定随机数生成市所用算法开始的整数值，
# 如果使用相同的seed( )值，则每次生成的随即数都相同，
# 如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。
random.seed(5)
num=0
while(num<5):
    print(random.random())
    num+=1

print("--------比较差异----------")

num=0
while(num<5):
    random.seed(5)
    print(random.random())
    num+=1




## 实例

import random
random.seed()
bandList=["华为","苹果","小米","联想","三星"]
i=random.randint(0,4)
print(f"随机的品牌为：{bandList[i]}")