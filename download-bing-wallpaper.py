#!/user/bin/env python

#coding:utf-8

import requests
import time

from bs4 import BeautifulSoup

from urllib.request import urlretrieve

base_url = 'https://cn.bing.com'

today_date = time.strftime( ('%Y%m%d') , time.localtime())

response = requests.get(base_url)

soup = BeautifulSoup(response.text, 'html.parser')

# 提取源代码中 data-ultra-definition-src 的属性值，然后拼贴到一起

pic_path = soup.find('div', attrs={'id': 'bgImgProgLoad'})['data-ultra-definition-src']

pic_url = base_url + pic_path

# 此处填写图片要保存的路径，例如我是放在 /Users/powersee/Documents/bing-wallpaper/ 这个文件夹里。
urlretrieve(url=pic_url, filename=r'/Users/powersee/Documents/bing-wallpaper/{}.jpg'.format(today_date))
