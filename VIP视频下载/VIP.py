# 用来爬取并下载VIP视频
# 首先选择要下载视频的URL 复制
# 其次网上找到全民vip视频解析,解析视频,并F12 收到.ts文件
from multiprocessing.pool import Pool

import requests


def temp(i):
    # 1. 找到url
    url = 'https://zkgn.wb699.com/2018/10/04/aVWM11EGdT3LsWoI/out%03d.ts'%i
    # 模拟浏览器访问
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
    }
    # 2. 解析url
    print(url)
    r = requests.get(url,headers=headers)
    # 3. 提取数据
    ret = r.content # 这个url的二进制数据  电影 音乐 图片 下载需要二进制数据
    with open('D:\达内python\PySpider\VIP视频下载\static\{}'.format(url[-10:]), 'wb') as f:
        f.write(ret)
if __name__ == '__main__':
    pool = Pool(20)
    for i in range(2000):
        pool.apply_async(temp, (i,))
    pool.close()
    pool.join()


