import requests

# 01-最基本
r=requests.get('https://w.wallhaven.cc/full/x8/wallhaven-x8582o.jpg')
with open('D:/Photos/num1.png','wb') as f:  # 二进制形式打开
    f.write(r.content)

# 02-加入headers传递头信息，添加User-Agent及其他字段信息
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
r=requests.get('https://w.wallhaven.cc/full/x8/wallhaven-x8582o.jpg',headers=headers)
with open('D:/Photos/num1.png','wb') as f:
    f.write(r.content)

# 03-利用urllib.request.Resquest()
import urllib
from urllib import request
url=urllib.request.Request('https://w.wallhaven.cc/full/6o/wallhaven-6ojo67.jpg') # Request()函数将url添加到头部，模拟浏览器访问
page=urllib.request.urlopen(url).read()  # 将url页面的源代码保存为字符串
open('D:/Photos/num2.png','wb').write(page)  # 写入

# 04-使用request.urlretrieve()函数下载
from urllib import request
request.urlretrieve('https://w.wallhaven.cc/full/6o/wallhaven-6ojo67.jpg','num2.png')  # 有些网站会开启反爬虫，则需要利用上面的方法传递headers


"""
  - 04-利用正则表达式爬取指定网页中的图片
"""

from bs4 import BeautifulSoup
import urllib.request
import re  # 正则表达式

def getpage(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    url=urllib.request.Request(url,headers=headers)
    page=urllib.request.urlopen(url).read()
    page=page.decode('UTF-8')
    return page

def getimage(page):  # 获取图片url,保存即可
    # imlist=re.findall(r'(https:[^\s]*?(jpg|jpeg|png|gif))',page)  # 正则表达式
    soup=BeautifulSoup(page,'html.parser')  # Beautifulsoup
    imlist=soup.find_all('img')
    x=0;
    for imurl in imlist:
        try:
            print(f'正在下载第{x}张图片,请耐心等待')
            urllib.request.urlretrieve(imurl.get('src'),'D:/Photos/%d.png'%x)
            x+=1
        except:
            continue

if __name__=='__main__':
    url=input('请输入想要提取图片的网址： ')
    page=getpage(url)
    getimage(page)

"""
  - 05-利用requests模块爬取搜狗图片
"""
import requests
import json
import urllib

def getsougouimage(category,length,path):
    n=length
    cate=category
    images=requests.get('https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?'
                        'category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))
    jd=json.loads(images.text)
    # print(jd)
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
    print('Doenload complete！')





# """
#   - 06-利用requests模块爬取百度图片
# """
# import requests
# from PIL import ImageFilter
# import re
#
# maxsearchpage=20
# currentpage=0
# defaultpath='D:/Photos/'
# needsave=0
#
# # 图片链接正则
# def imageurl(content):
#     return re.findall('"objURL":"(.*?)"',content,re.S)
#
# def nextsoure(content):
#     next=re.findall('<div id="page">.*<a href="(.*?)" class="n">',content,re.S)[0]
#     print("---------"+"https://image.baidu.com"+next)
#     return next
#
# # 爬虫主体
# def spidler(source):
#     content=requests.get(source).text
#     imagearr=ImageFilter(content)
#     global currentpage
#     print("Current page:"+str(currentpage)+'**************')
#     for imageUrl in imagearr:
#         print(imageUrl)
#         global needsave
#         if needsave:
#             global defaultpath
#             try:
#                 # 下载图片并设置超时时间，如果图片地址错误就不继续等待了
#                 picture=requests.get(imageUrl,timeout=10)
#             except:
#                 print('Download image error!errorUrl:'+imageUrl)
#                 continue
#
#             imageUrl=imageUrl.replace('/','').replace(':','').replace('?','')
#             picturesavepath=defaultpath+imageUrl
#             fp=open(picturesavepath,'wb')
#             fp.write(picture.content)
#             fp.close()
#     global maxsearchpage
#     if currentpage<=maxsearchpage:
#         if nextsoure(content):
#             currentpage+=1
#             spidler("https://image.baidu.com"+nextsoure(content))
#
# def beginsearch(page=1,save=0,savepath='D:/Photos/'):
#     # 页数、是否储存、默认储存路径
#     global maxsearchpage,needsave,defaultpath
#     maxsearchpage=page
#     needsave=save
#     defaultpath=savepath
#     key=input('输入关键字：')
#     startsource='https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+str(key)+'&ct=201326592&v=flip'
#     spidler(startsource)




















