import urllib.request
import re


def jiexi(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    url2 = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(url2).read()
    page = page.decode('UTF-8')
    # print(page)
    return page


def dl(page):
    htlist = re.findall(r'(https:[^\s]*?(jpg|png|gif|jpeg))', page)
    # print(htlist)
    x = 0
    for imglist in htlist:
        print(imglist)
        #for k in imglist:

        # try:
        #     print('正在下载：%s' % imglist[0])
        #     urllib.request.urlretrieve(imglist[0], 'D:/Photos/baidu/%d.jpg' % x)
        #     x += 2
        # except:
        #     continue


if __name__ == '__main__':
    url = 'https://image.baidu.com/search/index?ct=201326592&z=0&tn=baiduimage&ipn=r&word=%E5%A3%81%E7%BA%B8%20%E4%B8%8D%E5%90%8C%E9%A3%8E%E6%A0%BC%20%E5%94%AF%E7%BE%8E&pn=0' \
          '&istype=2&ie=utf-8&oe=utf-8&cl=2&lm=-1&st=-1&fr=&fmq=1567133149621_R&ic=0&se=&sme=&width=&height=&face=0&hd=0&latest=0&copyright=0'
    page = jiexi(url)
    dl(page)
