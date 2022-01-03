import numpy as np

data=[]
with open('C:/Users/NiKoJJ/Desktop/01.txt','r',encoding='utf-8') as f:
    for line in f:
        line=line.strip('\n')
        temp = line.split(',')
        data.append(temp)
        for i in range(len(data)):
            for j in range(6):
                data[i].append(float(data[i][j]))
            del(data[i][0:6])
        # print(temp)
        #for str_value in temp:
            #print(str_value)
        # print(line)
        for i in range(len(data)):
            L=data[i][0]
            M=data[i][1]
            print(L)
        max_l=max(int(L))
        max_m=max(int(M))
        C = np.array(max_l,max_m)
        S = np.array(max_l,max_m)
        for  i in range(len(data)):
            C[L,M]=data[i][2]
            S[L,M]=data[i][3]
        print(C)
        print('------------------')
        print(S)
