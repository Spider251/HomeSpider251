import requests
from fake_useragent import UserAgent

ua = UserAgent()

url = 'http://img1.imgtn.bdimg.com/it/u=2535062452,2075548441&fm=26&gp=0.jpg'
headers = {'User-Agent' : ua.ie}
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
img = res.content
with open('1.jpg', 'wb') as f:
    f.write(img)
