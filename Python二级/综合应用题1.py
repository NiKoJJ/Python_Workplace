#
#
# txt=open("D://test//命运.txt","r").read()
# for ch in "，。？！：":
#     txt=txt.replace(ch,"")
# d={}
# for ch in txt:
#     d[ch]=d.get(ch,0)+1
# ls=list(d.items())
# ls.sort(key=lambda x:x[1],reverse=True)
# a,b=ls[0]
# print("{}:{}".format(a,b))
#
# for i in range(10):
#     m,b=ls[i]
#     print(m,end="")

txt=open("D://test//命运.txt","r").read()
for ch in " \n":
    txt=txt.replace(ch,"")
d={}
for i in txt:
    d[i]=d.get(i,0)+1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
string=""
for i in range(len(ls)):
    s=str(ls[i]).strip("()")
    string=string+s[1]+":"+s[5]+","
f=open("命运-频次排序.txt","w")
f.write(string)
f.close()
