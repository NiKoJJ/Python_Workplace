import jieba
re=[]
txt="妈妈爱我"
new=jieba.lcut(txt)
print("".join(new[::-1]))

## zip函数
namelist=["xiaoming","lihua",'niuniu',"xiaoli"]
numlist=["001","002","003","004"]
for name,num in zip(namelist,numlist):
    print(f"{name}:{num}")

## 定义一个求和函数

def calc_sum(*kwg):
    ax=0
    for i in kwg:
        ax=ax+i
    return ax


print(calc_sum(1,2,3,4,5))

##  异常处理
def mult_exception(x,y):
    try:
        a=x/y
        b=name
    except ZeroDivisionError:
        print("Zore error")
    except NameError:
        print(' ')