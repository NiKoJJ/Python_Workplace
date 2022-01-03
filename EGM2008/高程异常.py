import pandas as pd
import numpy as np



# with open('C:/Users/NiKoJJ/Desktop/EGM2008.gfc','r') as f:
#     df=f.readlines()
#     # print(df)
#     print(type(df))
#     # print(df.size)
#     new=df[1].split(",")
#     print(new)

def loaddata(inputfile):
    f=open(inputfile,'r')
    sourcelines=f.readlines()
    dataset=[]
    for line in sourcelines:
        temp1=line.strip('\n')
        temp2=temp1.split('\r')
        dataset.append(temp2)
    return dataset

inputfile='C:/Users/NiKoJJ/Desktop/EGM2008.txt'
file=loaddata(inputfile)