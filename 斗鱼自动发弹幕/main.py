'''
2019-01-05  12:25
2019-01-05  15:15
有个BUG在注释的那里,登录需要图片验证
根据用户输入的视频分类,得出所有的房间号,用户输入房间号进入直播间,用户输入弹幕并输入每次发送的间隔发送弹幕
title 英雄联盟
room 911
barrage 这是一条弹幕
btime 5s

所有分类的xpath://ul[@class="btns"]/li/a/@href


<a class="bottom-classifyOneEach" target="_blank" title="英雄联盟" href="/g_LOL">英雄联盟</a>
<a class="bottom-classifyOneEach" target="_blank" title="炉石传说" href="/g_How">炉石传说</a>
<a class="bottom-classifyOneEach" target="_blank" title="dota2" href="/g_DOTA2">dota2</a>
<a class="bottom-classifyOneEach" target="_blank" title="棋牌娱乐" href="/g_qipai">棋牌娱乐</a>
<a class="bottom-classifyOneEach" target="_blank" title="dnf" href="/g_DNF">dnf</a>
<a class="bottom-classifyOneEach" target="_blank" title="穿越火线" href="/g_CF">穿越火线</a>
<a class="bottom-classifyOneEach" target="_blank" title="守望先锋" href="/g_Overwatch">守望先锋</a>
<a class="bottom-classifyOneEach" target="_blank" title="堡垒之夜" href="/g_blzy">堡垒之夜</a>
<a class="bottom-classifyOneEach" target="_blank" title="CS:GO" href="/g_CSGO">CS:GO</a>
<a class="bottom-classifyOneEach" target="_blank" title="QQ飞车" href="/g_qqfcdy">QQ飞车</a>
<a class="bottom-classifyOneEach" target="_blank" title="逆水寒" href="/g_nsh">逆水寒</a>
<a class="bottom-classifyOneEach" target="_blank" title="魔兽世界" href="/g_WOW">魔兽世界</a>

'''

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


base_url = 'https://www.douyu.com'
res = requests.get(base_url)
res.encoding = 'utf-8'
html = res.text
print(html)
soup = BeautifulSoup(html, 'lxml')
key = input("请输入要选择的分类:")
# title_href 为/g_LOL
title_href = soup.find_all('a', attrs={'title': key})[0].get('href')
# 下面这个url为分类的url
url = base_url + title_href
# 访问分类页面
res = requests.get(url)
res.encoding = 'utf-8'
html = res.text
soup = BeautifulSoup(html)
# room房间号
room_id_List = soup.find_all('a', attrs={'class': 'play-list-link'})
print(room_id_List)
L = []
for room_id in room_id_List:
    room_id = room_id.get('href')
    L.append(room_id)
    # 所有的房间找到了,进入id
print(L)
room = input("选择进入的房间号:")
driver = webdriver.Chrome()
driver.get(base_url+'/'+room)
time.sleep(10)
'''
if driver.page_source.find('MuteStatus-isLog') != -1:
    # 点击登录
    driver.get('https://passport.douyu.com/index/login')
    # driver.find_element_by_class_name('MuteStatus-isLog').click()
    print("正在登录")
    # driver.find_element_by_class_name('scancide-to js-to-link js-need-param fr').click()
    # print("点击密码登录成功")
    driver.find_element_by_class_name('fr ipt ipt-need-parent country-phonenum').send_keys('15513602071')
    print("输入账号成功")
    driver.find_element_by_class_name('ipt').send_keys('tt2008gax')
    print("输入密码成功")
    driver.find_element_by_class_name('loginbox-sbt btn-sub').click()
    print("登录成功")
    # 需要图片拖动验证,没完成
'''
barrage = input("输入的内容:")
barrage_time = int(input("每条弹幕的间隔:"))
num = 1
while True:
    driver.find_element_by_class_name('ChatSend-txt').send_keys(barrage)
    driver.find_element_by_class_name('ChatSend-button ').click()
    print("发送第%d条弹幕成功"%num)
    time.sleep(barrage_time)
    if num == 3:
        break
    num += 1
