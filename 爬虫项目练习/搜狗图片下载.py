import requests
import json
import urllib


def getsougouimage(category,length,path):
    n=length
    cate=category
    images=requests.get('https://pic.sogou.com/pics?query='+cate)
    jd=images.text
    print(jd.encode())
    jd=jd['all_items']
    images_url=[]  # list
    for j in jd:
        # print(j)
        images_url.append(j['bthumbUrl'])  # 依次添加
    m=0
    for image_url in images_url:
        print('*****'+str(m)+'.jpg *b****'+'Downloading...')
        urllib.request.urlretrieve(image_url,path+str(m)+'.jpg')
        m=m+1
    print('Download complete！')


getsougouimage('奥运',300,'D:/Program/爬虫结果')

