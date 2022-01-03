fi=open("D:\\new.txt","rb")
fo=open("D:\\earpa001.txt","wt")
for line in fi:
    ls=str(line,encoding="utf-8").strip('\r\n').split(',')
    if ls[1].count("earpa001")>0:
        fo.write("{},{},{},{}\n".format(ls[0],ls[1],ls[2],ls[3]))
fi.close()
fo.close()

f=open("D:\\earpa001.txt","r")
fo=open("D:\\result.txt","w")
d={}
for line in f:
    t=line.strip("\n").split(",")
    s=t[2]+"-"+t[3]
    d[s]=d.get(s,0)+1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(len(ls)):
    a,b=ls[i]
    fo.write("{},{}".format(a,b))
f.close()
fo.close()