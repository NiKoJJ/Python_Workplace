import time


## 获取当前时间戳
t1=time.time()
print(t1)

## 获取可读的时间 cuurent_time
t2=time.ctime()
print(t2)

## 获取struct_time格式的时间
t3=time.gmtime()
print(t3)

## 将gmtime() 按照想要的格式打印出来
t4=time.strftime("%Y-%m-%d  %H:%M:%S:%p",t3)
print(t4)


## 将可读的时间转换为struct_time格式
timeStr="2021-9-25 11:19:25"
t5=time.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
print(t5)