n=eval(input("请输入一串字符："))
print(f'输入的数为：{n}')
print(type(n))
print("{:,}".format(n))
print("{:->20}".format("{:,}".format(n)))  ## 右对齐 千分位逗号分隔符
print("{:-^20}".format(n))  ## 居中对其
print("{:-<20}".format(n))  ## 左对齐