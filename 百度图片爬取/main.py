import random
import requests
from fake_useragent import UserAgent
import re
import time

ua = UserAgent()

class BaiDuSpider:
    def __init__(self):
        self.headers = {'User-Agent': ua.random}
        self.pn = 30
        self.rn = 0
        self.num = 0
        self.url = 'http://image.baidu.com/search/index?tn=baiduimage&cl=2&ie=gb18030&word=%C3%C0%C5%AE%CD%BC%C6%AC'

    def getPage(self,params):
        res = requests.get(self.url,params=params,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        # print(html)
        self.parsePage(html)
    def parsePage(self,html):
        p = re.compile('"thumbURL":"(.*?)"',re.S)
        rList = p.findall(html)
        self.write(rList)
    def write(self,rList):
        # 对每一张图片发起请求
        for list in rList:
            print(list)
            res = requests.get(list,headers={'User-Agent': ua.random})
            img = res.content
            print(res.text)
            with open(str(self.num)+'.png','wb') as f:
                f.write(img)
                time.sleep(random.randint(1,5))
                print("第%s页下载成功!"%str(self.num))
            self.num += 1
    def main(self):
        pn = int(input("请输入要下载的页数:"))
        for i in range(0,pn):
            params = {
                'tn': 'resultjson_com',
                'ipn': 'rj',
                'ct': '201326592',
                'is':'',
                'fp': 'result',
                'queryWord': '美女图片',
                'cl': '2',
                'lm': '',
                'ie': 'utf-8',
                'oe': 'utf-8',
                'adpicid': '',
                'st': '',
                'z': '',
                'ic': '',
                'hd': '',
                'latest': '',
                'copyright': '',
                'word': '美女图片',
                's': '',
                'se': '',
                'tab': '',
                'width': '',
                'height': '',
                'face': '',
                'istype': '',
                'qc': '',
                'nc': '',
                'fr': '',
                'expermode': '',
                'force': '',
                'cg': 'girl',
                'pn': self.pn*i,
                'rn': self.rn*i,
                'gsm': '78',
                '1546223995849':''
            }
            self.getPage(params)

if __name__ == '__main__':
    spider = BaiDuSpider()
    spider.main()
