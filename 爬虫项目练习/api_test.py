import requests

url="https://www.imguz.cn/api/upload_config"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
re=requests.get(url,headers=headers)
print(re.content)